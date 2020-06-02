__author__ = "akashjeez"

import requests, pandas
import re, random, itertools
from datetime import datetime, timedelta


def covid19_usa_stats():
	'''Get LIVE CoronaVirus Stats From United States of America!'''
	try:
		response = requests.get("https://corona.lmao.ninja/v2/states")
		dataset = [{
			'state': data.get('state', 'TBD'), 
			'total_cases': data.get('cases', 'TBD'), 
			'today_cases': data.get('todayCases', 'TBD'), 
			'total_deaths': data.get('deaths', 'TBD'), 
			'today_deaths': data.get('todayDeaths', 'TBD'), 
			'acive_cases': data.get('active', 'TBD'), 
		} for data in response.json()]
		return {'count': len(dataset), 'data': dataset}
	except Exception as ex:
		return {"Error": ex}


def covid19_stats():
	'''Get LIVE CoronaVirus Stats From All Over Globe!'''
	try:
		BASE_URL = "https://covid.ourworldindata.org/data"
		covid_data = pandas.read_csv(f"{BASE_URL}/ecdc/full_data.csv")
		population_data = pandas.read_csv(f"{BASE_URL}/ecdc/locations.csv")
		new_df = pandas.merge(covid_data, population_data, on = 'location', how = 'left')
		new_df.drop(['countriesAndTerritories', 'population'], axis = 1, inplace = True)
		new_df = new_df[ new_df.population_year == 2020.0]
		new_df['population_year'] = new_df['population_year'].astype(int)
		dataset = [{
			'date': data[0], 
			'country': data[1], 
			'new_cases': data[2], 
			'new_deaths': data[3], 
			'total_cases': data[4], 
			'total_deaths': data[5], 
			'continent': data[6]
		} for data in new_df.values.tolist() ]
		return {'count': len(dataset), 'data': dataset}
	except Exception as ex:
		return {"Error": ex}

def google_place(location):
	'''Get Coordinates From Google for Input Location'''
	try:
		BASE_URL, API_KEY = 'https://maps.googleapis.com/maps/api', 'AIzaSyDCpf9LE6ZnVxzTxC6TbZ3Dc_Ro91pdra4'
		request_url = f"{BASE_URL}/place/findplacefromtext/json?input={location.replace(' ', '+')}"
		request_url += f"&inputtype=textquery&fields=formatted_address,name,rating,opening_hours,geometry"
		response = requests.get(f"{request_url}&key={API_KEY}").json()
		dataset = {
			'name': response['candidates'][0].get('name', 'TBD'), 
			'address': response['candidates'][0].get('formatted_address', 'TBD'),
			'open_now?': response['candidates'][0]['opening_hours'].get('open_now', 'TBD'), 
			'coordinates': response['candidates'][0]['geometry'].get('location', 'TBD'),
			'rating': response['candidates'][0].get('rating', 'TBD'),
		} if response['status'] == 'OK' else {'error': 'Invalid Requests / Zero Results!'}
		return dataset
	except Exception as ex:
		return f"Error: {ex}"


def public_holidays(country):
	''' Get Public Holidays for a Country using Public API '''
	try:
		BASE_URL, dataset, year = "https://date.nager.at", [], datetime.now().year
		data_dump_1 = pandas.read_html(f"{BASE_URL}/Home/Countries")[0].values.tolist()
		countries_dict = {data[0]: data[1] for data in data_dump_1 if data[0] != 'Namibia' }
		print(f"\n Countries: \n {countries_dict} \n")
		for country_name, country_code in countries_dict.items():
			if country_name.startswith(country.capitalize()):
				data_dump_2 = requests.get(f"{BASE_URL}/api/v2/PublicHolidays/{year}/{country_code}")
				dataset = [{
					'country_name': country_name,
					'holiday_date': data['date'], 
					'holiday_name': data['name'], 
					'holiday_type': data['type'],
					'is_global': 'Yes' if data['global'] == True else 'No'
				} for data in data_dump_2.json()]
		return {'count': len(dataset), 'data': dataset}
	except Exception as ex:
		return f"Error: {ex}"


def fuel_price():
	''' Get Live Fuel (Petrol, Diesel) Price in India from https://www.goodreturns.in '''
	try:
		BASE_URL = "https://www.goodreturns.in"
		data_dump_1 = pandas.read_html(f"{BASE_URL}/petrol-price.html")[0].values.tolist()[1:]
		data_dump_2 = pandas.read_html(f"{BASE_URL}/diesel-price.html")[0].values.tolist()[1:]
		dataset = [{
			'state': data[0][0], 'petrol_price_today': data[0][1], 'petrol_price_yesterday': data[0][2],
			'diesel_price_today': data[1][1], 'diesel_price_yesterday': data[1][2]
		} for data in zip(data_dump_1, data_dump_2)]
		return {'count': len(dataset), 'last_updated': datetime.now().strftime('%d-%b-%Y'), 'data': dataset}
	except Exception as ex:
		return f"Error: {ex}"

def flames_game(male_name, female_name):
	try:
		def flames_count(male_name, female_name):
			male_name_list = list(male_name)
			female_name_list = list(female_name)
			for letter in male_name_list[:]:
				if female_name_list.count(letter) > 0:
					female_name_list.remove(letter)
					male_name_list.remove(letter)
			return len(female_name_list) + len(male_name_list)

		def flames_result(count):
			flames_list = ['Friend', 'Love', 'Affection', 'Marriage', 'Enemy', 'Sister']
			while len(flames_list) > 1:
				remove_count = count
				if count > len(flames_list):
					remove_count = count % len(flames_list)
					if remove_count == 0:
						remove_count = len(flames_list)
				flames_list.remove(flames_list[remove_count - 1])
				flames_list = flames_list[remove_count - 1:] + flames_list[:remove_count - 1]
			return flames_list[0]

		def calculate(male_name, female_name):
			first_name = male_name.lower().replace(' ', '')
			second_name = female_name.lower().replace(' ', '')
			return flames_result(flames_count(first_name, second_name))

		result = calculate(male_name, female_name)
		return {'male_name': male_name, 'female_name': female_name, 'result': result}
	except Exception as ex:
		return f"Error: {ex}"


def age_calculator(input_dob):
	''' Calculate Age by Passing Date of Birth as Input. '''
	try:
		b_date = datetime.strptime(input_dob, '%d-%m-%Y')
		age_calc = round(((datetime.today() - b_date).days/365), 2)
		return {"dob": input_dob, "age": age_calc}
	except Exception as ex:
		return f"Error: {ex}"	


def shuffle_cards():
	''' Shuffle of Cards Randomly! '''
	try:
		## Make a Deck of Cards
		deck = list(itertools.product(range(1, 14), ['Spade', 'Heart', 'Diamond', 'Club']))
		## Shuffle the Cards
		random.shuffle(deck)
		return [f"{deck[i][0]} of {deck[i][1]}" for i in range(5)]
	except Exception as ex:
		return f"Error: {ex}"


def dns_search(dns_name):
	''' Search Public DNS Info from http://dns.google.com '''
	try:
		response = requests.get(f"https://dns.google.com/resolve?name={dns_name.lower()}").json()
		return {"dns_name": dns_name, "results": [ip_address['data'] for ip_address in response['Answer']]}
	except Exception as ex:
		return f"Error: {ex}"	


def bookmyshow(city_name):
	''' Get Latest & Upcoming Movies Type & Name Data from BookMyShow.com '''
	try:
		NOW_SHOWING_REGEX = """{"event":"productClick","ecommerce":{"currencyCode":"INR","click":{"actionField":{"list":"Filter Impression:category\\\/now showing"},"products":\[{"name":"(.*?)","id":"(.*?)","category":"(.*?)","variant":"(.*?)","position":(.*?),"dimension13":"(.*?)"}\]}}}"""
		COMING_SOON_REGEX = """{"event":"productClick","ecommerce":{"currencyCode":"INR","click":{"actionField":{"list":"category\\\/coming soon"},"products":{"name":"(.*?)","id":"(.*?)","category":"(.*?)","variant":"(.*?)","position":(.*?),"dimension13":"(.*?)"}}}}"""
		if city_name is not None:
			response = requests.get(f"https://in.bookmyshow.com/{city_name.lower()}/movies", headers = {'User-Agent' : "Magic Browser"})
			showing_movies = [{
				"movie_name": data[0], "movie_id": data[1], "movie_type": data[3], "movie_language": data[5]
			} for data in re.findall(NOW_SHOWING_REGEX, response.text)]
			upcoming_movies = [{
				"movie_name": data[0], "movie_id": data[1], "movie_type": data[3], "movie_language": data[5]
			} for data in re.findall(COMING_SOON_REGEX, response.text)]
			return {"showing_movies": showing_movies, "upcoming_movies": upcoming_movies}
		else:
			return "Please Enter Valid City Name to Get Latest / Upcoming Movies List!"
	except Exception as ex:
		return f"Error: {ex}"	


def open_trivia():
	''' Get Latest Open Trivia Q&A Data using Public API (https://opentdb.com/api.php) '''
	try:
		response = requests.get('https://opentdb.com/api.php?amount=10').json()
		return {'count': len(response['results']), 'data': response['results']}
	except Exception as ex:
		return f"Error: {ex}"


def file_formats():
	''' Get All File Formats Data using Public API (http://vocab.nic.in/rest.php) '''
	try:
		response = requests.get('http://vocab.nic.in/rest.php/format/json').json()
		dataset = [{
			"format_name": data['format']['format_name'],
			"format_description": data['format']['format_desc']
		} for data in response['formats']]
		return {'count': len(dataset), 'data': dataset}
	except Exception as ex:
		return f"Error: {ex}"


def get_nobel_prize():
	''' Get Latest Nobel Prize Data using Public API (http://api.nobelprize.org) '''
	try:
		response = requests.get('http://api.nobelprize.org/v1/prize.json').json()
		return {'count': len(response['prizes']), 'data': response['prizes']}
	except Exception as ex:
		return f"Error: {ex}"


def car_maker_manufacturers():
	''' Get All Cars Makers & Manufacturers Data using Public API (https://vpic.nhtsa.dot.gov/api) '''
	try:
		BASE_URL = "https://vpic.nhtsa.dot.gov/api/vehicles"
		response_1 = requests.get(f"{BASE_URL}/getallmakes?format=json").json()
		response_2 = requests.get(f"{BASE_URL}/getallmanufacturers?format=json").json()
		return {'makers': response_1['Results'], 'manufacturers': response_2['Results']}
	except Exception as ex:
		return f"Error: {ex}"


def random_user_generator():
	''' Get a Random Fake User Data using Public API (https://uinames.com/api) '''
	try:
		return requests.get("https://uinames.com/api/?ext").json()
	except Exception as ex:
		return f"Error: {ex}"


def movie_search(movie_name):
	''' Get Movie Infromation using Public API (http://www.omdbapi.com)  '''
	try:
		response = requests.get(f"http://www.omdbapi.com/?apikey=80440342&t={movie_name.lower()}").json()
		if response['Response'] == 'True':
			dataset = {
				"movie_name": response['Title'], "year": response['Year'], "poster_url": response['Poster'],
				"release_date": response['Released'], "duration": response['Runtime'], "genre": response['Genre'], 
				"director": response['Director'], "writer": response['Writer'],"actors": response['Actors'], 
				"plot": response['Plot'], "language": response['Language'],"country": response['Country'], 
				"awards": response['Awards'], "imdb_rating": response['imdbRating'],"imdb_votes": response['imdbVotes'], 
				"imdb_id": response['imdbID'], "type": response['Type'], "website": response['Website'], 
				"ratings": response['Ratings'],
			}
			return dataset
		else:
			return "Movie Not Found, Please Try Again!"
	except Exception as ex:
		return f"Error: {ex}"


def comic_books_data():
	''' Get New Comic Book Data using Public API (https://api.shortboxed.com/) '''
	try:
		response = requests.get('https://api.shortboxed.com/comics/v1/new').json()
		dataset = [{
			"title": data['title'],
			"description": data['description'],
			"publsher": data['publsher'],
			"price": data['price'],
			"release_date": data['release_date'],
			"creators": data['creators'] 
		} for data in response['comics']]
		return {'count': len(dataset), 'data': dataset}
	except Exception as ex:
		return f"Error: {ex}"

def get_country_info():
	''' Get Country Info like COuntry Code, capital, ISO & Phone Code using Public API (http://country.io). '''
	try:
		dataset = []
		country_names = requests.get("http://country.io/names.json").json()
		country_capitals = requests.get("http://country.io/capital.json").json()
		iso_codes = requests.get("http://country.io/iso3.json").json()
		phone_codes = requests.get("http://country.io/phone.json").json()
		for country_code, country_name in country_names.items():
			for code1, country_capital in country_capitals.items():
				for code2, iso_code in iso_codes.items():
					if (country_code == code1) & (country_code == code2):
						for code3, phone_code in phone_codes.items():
							if code3 == country_code:
								dataset.append({"country_code": country_code,
									"country_name": country_name, "country_capital": country_capital,
									"iso_code": iso_code, "phone_code": phone_code
								})
		return {'count': len(dataset), 'data': dataset}
	except Exception as ex:
		return f"Error: {ex}"


def cloud_compute_cost(provider, input_cpu, input_memory, input_region):
	''' 
		Get Cloud Compute Pricing from Public API (https://banzaicloud.com/cloudinfo/) for Cloud providers 
		like Aamzon AWS Cloud, Alibaba Cloud, Google Cloud Platform, Microsoft Azure Cloud.
	'''
	try:
		dataset = []
		BASE_URL = "https://banzaicloud.com/cloudinfo/api/v1/providers"
		regions_data = requests.get(f"{BASE_URL}/{provider.casefold()}/services/compute/regions").json()
		regions_data = [{'id': data['id'], 'name': data['name']} for data in regions_data if data['id'] != 'uaenorth']
		for region in regions_data:
			response = requests.get(f"{BASE_URL}/{provider.casefold()}/services/compute/regions/{region['id']}/products").json()
			for product in response['products']:
				data = {
					'category': product['category'], 
					'instance_type': product['type'],
					'cpu': int(product['cpusPerVm']),
					'memory': round(float(product['memPerVm']),1),
					'cost': round(float(product['onDemandPrice']),3),
					'region_id': region['id'],
					'region_name': region['name'],
					'network_performance': product['ntwPerf'],
					'network_performance_category': product['ntwPerfCategory']
				}
				if data['cpu'] == int(input_cpu) and data['memory'] <= float(input_memory):
					input_region = "" if input_region.startswith('all') else input_region
					if (input_region in data['region_name'].casefold()):
						dataset.append(data)
		return {'count': len(dataset), 'data': dataset}
	except Exception as ex:
		return f"Error: {ex}"


def get_weather_data(city_name):
	''' Get Live & Forecast Weather Report Data for Any Location from Public API (https://metaweather.com/api/)'''
	try:
		BASE_URL = "https://www.metaweather.com/api/location"
		response_1 = requests.get(f"{BASE_URL}/search", params = {'query': city_name.lower()}).json()
		if len(response_1):
			response_2 = requests.get(f"{BASE_URL}/{response_1[0]['woeid']}/").json()
			dataset = {
				"location_id": response_2['woeid'],
				"location_name": response_2['title'],
				"location_type": response_2['location_type'],
				"latitude": response_2['latt_long'].split(',')[0],
				"longitude": response_2['latt_long'].split(',')[1],
				"timezone": response_2['timezone'],
				"sunrise_datetime": datetime.strptime(response_2['sun_rise'][:19], '%Y-%m-%dT%H:%M:%S').strftime('%d-%m-%Y %I:%M %p'),
				"sunset_datetime": datetime.strptime(response_2['sun_set'][:19], '%Y-%m-%dT%H:%M:%S').strftime('%d-%m-%Y %I:%M %p'),
				"country": {
					"country_id": response_2['parent']['woeid'],
					"country_name": response_2['parent']['title'],
					"country_latitude": response_2['parent']['latt_long'].split(',')[0],
					"country_longitude": response_2['parent']['latt_long'].split(',')[1],
				},
				"data": [{
					"weather_date": datetime.strptime(data['applicable_date'], '%Y-%m-%d').strftime('%d-%m-%Y'),
					"weather_state": data['weather_state_name'],
					"temperature": round(int(data['the_temp']), 2),
					"minimum_temperature": round(int(data['min_temp']), 2),
					"maximum_temperature": round(int(data['max_temp']), 2),
					"wind_speed": round(int(data['wind_speed']), 2),
					"wind_direction": round(int(data['wind_direction']), 2),
					"air_pressure": round(int(data['air_pressure']), 2),
					"humidity": data['humidity'],
					"visibility": round(int(data['visibility']), 2),
					"predictability": round(int(data['predictability']), 2)
				} for data in response_2['consolidated_weather']]
			}
			return dataset
		else:
			return "Location Not Found, Please try again!"
	except Exception as ex:
		return f"Error: {ex}"


def say_hello(name = None):
	''' Greetings to User! '''
	if name is None:
		return "Hello, World!"
	else:
		return f"Hello, {name}!"

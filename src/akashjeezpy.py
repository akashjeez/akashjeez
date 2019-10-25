__author__ = "akashjeez"

import requests
from datetime import datetime, timedelta


def cloud_compute_cost(provider, input_cpu, input_memory, input_region):
	''' 
		Get Cloud Compute Pricing from Public API (https://banzaicloud.com/cloudinfo/) for Cloud providers 
		like Aamzon AWS Cloud, Alibaba Cloud, Google Cloud Platform, Microsoft Azure Cloud.
	'''
	try:
		dataset = []
		base_url = "https://banzaicloud.com/cloudinfo/api/v1/providers"
		regions_data = requests.get(f"{base_url}/{provider.casefold()}/services/compute/regions").json()
		regions_data = [{'id': data['id'], 'name': data['name']} for data in regions_data if data['id'] != 'uaenorth']
		for region in regions_data:
			response = requests.get(f"{base_url}/{provider.casefold()}/services/compute/regions/{region['id']}/products").json()
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
		base_url = "https://www.metaweather.com/api/location"
		response_1 = requests.get(f"{base_url}/search", params = {'query': city_name.lower()}).json()
		if len(response_1):
			response_2 = requests.get(f"{base_url}/{response_1[0]['woeid']}/").json()
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
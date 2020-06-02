# akashjeezpy

akashjeezpy is a Python Package to Deliver a Lot of Useful Services!

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install akashjeezpy.

```bash
pip install akashjeezpy
```

## Usage

```python

import akashjeezpy

## Check Attributes and Methods available in this package.
print(dir(akashjeezpy)) # returns list of attributes and methods of this module.

## Service: Greetings to User!
print(akashjeezpy.say_hello()) # returns 'Hello, World!'
print(akashjeezpy.say_hello("Everyone")) # returns 'Hello, Everyone!'

## Service: Get Coordinates From Google for Input Location
# Syntax: >> google_place(location)
print(akashjeezpy.google_place('queensland chennai'))

## Service: Get LIVE CoronaVirus Stats From United States of America!
print(akashjeezpy.covid19_usa_stats())

## Service: Get LIVE CoronaVirus Stats From All Over Globe!
print(akashjeezpy.covid19_stats())

## Service: Get Cloud Compute Pricing from Public API.
# Syntax: >> cloud_compute_cost(provider, input_cpu, input_memory, input_region)
# Providers = alibaba, amazon, azure, google 
# Input Regions = all, US, EU, Asia etc
print(akashjeezpy.cloud_compute_cost('azure', 2, 4, 'asia'))
print(akashjeezpy.cloud_compute_cost('amazon', 2, 4, 'us'))

## Service: Get Live & Forecast Weather Report Data for Any Location from Public API.
# Syntax: >> get_weather_data(city_name)
print(akashjeezpy.get_weather_data('chennai'))
print(akashjeezpy.get_weather_data('los angeles'))

## Service: Get Country Info like COuntry Code, capital, ISO & Phone Code using Public API .
print(akashjeezpy.get_country_info())

## Service: Get New Comic Book Data using Public API.
print(akashjeezpy.comic_books_data())

## Service: Get Movie Infromation using Public API.
# Syntax: >> movie_search(movie_name)
print(akashjeezpy.movie_search('furious'))

## Service: Get a Random Fake User Data using Public API.
print(akashjeezpy.random_user_generator())

## Service: Get All Cars Makers & Manufacturers Data using Public API.
print(akashjeezpy.car_maker_manufacturers())

## Service: Get Latest Nobel Prize Data using Public API.
print(akashjeezpy.get_nobel_prize())

## Service: Get All File Formats Data using Public API.
print(akashjeezpy.file_formats())

## Service: Get Latest Open Trivia Q&A Data using Public API.
print(akashjeezpy.open_trivia()

## Service: Get Latest & Upcoming Movies Type & Name Data from BookMyShow.com
# Syntax: >> bookmyshow(city_name)
print(akashjeezpy.bookmyshow('chennai'))

## Service: Search Public DNS Info from http://dns.google.com
print(akashjeezpy.dns_search('akashjeez.herokuapp.com')

## Serice: Shuffle of Cards Randomly!
print(akashjeezpy.shuffle_cards())

## Service: Calculate Age by Passing Date of Birth as Input.
# Syntax: >> age_calculator(input_dob)
print(akashjeezpy.age_calculator('10-04-1993'))

```


## Contributing
Pull Requests are Welcome. For Major Changes, Please Open an issue First to Discuss What You Would like to Change.

Please Make Sure to Update Tests as Appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
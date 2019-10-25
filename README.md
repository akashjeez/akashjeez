# akashjeezpy

akashjeezpy is a Python Package to Deliver a Lot of Useful Services!

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install akashjeezpy.

```bash
pip install akashjeezpy
```

## Usage

## Check Attributes and Methods available in this package.

```python

import akashjeezpy

print(dir(akashjeezpy)) # returns list of attributes and methods of this module.

```

## Service: Greetings to User!

```python

import akashjeezpy

# Pass any name as argument to say_hello() to greet!
print(akashjeezpy.say_hello()) # returns 'Hello, World!'
print(akashjeezpy.say_hello("Everyone")) # returns 'Hello, Everyone!'

```

## Service: Get Cloud Compute Pricing from Public API.

```python

import akashjeezpy

# Syntax: >> cloud_compute_cost(provider, input_cpu, input_memory, input_region)
# Providers = alibaba, amazon, azure, google 
# Input Regions = all, US, EU, Asia etc
print(akashjeezpy.cloud_compute_cost('azure', 2, 4, 'asia'))
print(akashjeezpy.cloud_compute_cost('amazon', 2, 4, 'us'))

```

## Service: Get Live & Forecast Weather Report Data for Any Location from Public API.

```python

import akashjeezpy

# Syntax: >> get_weather_data(city_name)
print(akashjeezpy.get_weather_data('chennai'))
print(akashjeezpy.get_weather_data('los angeles'))

```



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
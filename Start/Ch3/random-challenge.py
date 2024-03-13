import json
import random
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

month = '05'
year = '2017'


def is_year_month(d, year, month):
    year_month = year + '-' + month
    if d['date'][0:7] == year_month:
        return True
    else:
        return False


days = list(filter(lambda d: is_year_month(d=d, year=year, month=month), weatherdata))

rnd_days = random.choices(days, k=5)
pprint.pp(rnd_days)

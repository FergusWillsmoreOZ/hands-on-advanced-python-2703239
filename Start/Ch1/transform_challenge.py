

import json
import copy
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

Avg_Temp = lambda t1, t2: (t1 + t2) / 2.0

def avg_temp_to_desc(d):
    atmp = Avg_Temp(d['tmax'], d['tmin'])
    if atmp <= 60:
        desc = 'cold'
    elif atmp >= 80:
        desc = 'hot'
    else:
        desc = 'warm'
    return (d['date'], desc)

tuple_data = list(map(avg_temp_to_desc, weatherdata))
pprint.pp(tuple_data)
print(type(tuple_data))
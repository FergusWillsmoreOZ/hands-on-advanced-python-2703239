import json
import pprint
from functools import reduce

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)


def misery_score(d):
    wind = 0 if d['awnd'] is None else d['awnd']
    temp = d['tmax'] * 0.8
    rain = d['prcp'] * 10
    score = (wind + temp + rain) / 3
    return score


def most_miserable(acc, elem):
    return elem if misery_score(elem) >= misery_score(acc) else acc


result = reduce(most_miserable, weatherdata)
pprint.pp(result)

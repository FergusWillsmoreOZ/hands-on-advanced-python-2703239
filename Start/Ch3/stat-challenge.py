

import json
import statistics

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

winters = ["-12-", "-01-", "-02-"]
winter_months = [d for d in weatherdata if any([month in d['date'] for month in winters])]

avg_temps = [(d['tmax']+d['tmin'])/2 for d in winter_months]
print(statistics.stdev(avg_temps))
upper_outlier = statistics.mean(avg_temps) + statistics.stdev(avg_temps) * 2

outliers = [t for t in avg_temps if t >= upper_outlier]
print(len(outliers))


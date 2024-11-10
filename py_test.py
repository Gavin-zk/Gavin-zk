import pandas as pd

def uncertainty_co2_per_capita(data, year, k):
    result = {}
    countries = data['country'].unique()
    for country in countries:
        country_data = data[data['country'] == country]
        emissions = []
        for i in range(2, k + 1):
            if year - i in country_data['year'].values:
                emissions.append(country_data[country_data['year'] == year - i]['co2_per_capita'].values[0])
        if emissions:
            sorted_emissions = sorted(emissions)
            n = len(emissions)
            lower_index = int(n * 0.1)
            upper_index = int(n * 0.9)
            median_index = n // 2
            median = sorted_emissions[median_index]
            tenth_percentile = sorted_emissions[lower_index]
            ninetieth_percentile = sorted_emissions[upper_index]
            result[country] = (median, tenth_percentile, ninetieth_percentile)
    return result





data = pd.read_csv('owid-co2-data.csv')
year = 2024
k = 10
result = uncertainty_co2_per_capita(data, year, k)
print(result)
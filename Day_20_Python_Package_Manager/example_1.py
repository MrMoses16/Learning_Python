import requests
import numpy as np
import pandas as pd

# Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
# the min, max, mean, median, standard deviation of cats' weight in metric units.
# the min, max, mean, median, standard deviation of cats' lifespan in years.
# Create a frequency table of country and breed of cats

url = 'https://api.thecatapi.com/v1/breeds'

response = requests.get(url)
cat_info = response.json()

weights = []
lifespans = []
countries = []

for cat in cat_info:
    weight_range = cat.get("weight", {}).get("metric", "")
    weights.append(int(w) for w in weight_range.split(" - "))
    
    lifespan_range = cat.get("lifespan", "")
    lifespans.append(int(life) for life in lifespan_range.split(" - "))

    countries.append((cat.get("origin", 'unknown'), cat.get('name', 'unknown')))

# Flatten the weights and lifespans for statistics
weights_flat = [item for sublist in weights for item in sublist]
lifespans_flat = [item for sublist in lifespans for item in sublist]

# Calculate statistics
weight_stats = {
    "min": np.min(weights_flat),
    "max": np.max(weights_flat),
    "mean": np.mean(weights_flat),
    "median": np.median(weights_flat),
    "std": np.std(weights_flat)
}

lifespan_stats = {
    "min": np.min(lifespans_flat),
    "max": np.max(lifespans_flat),
    "mean": np.mean(lifespans_flat),
    "median": np.median(lifespans_flat),
    "std": np.std(lifespans_flat)
}

# Create frequency table for countries and breeds
country_breed_table = pd.DataFrame(countries, columns=["Country", "Breed"]).value_counts()

# Print results
print("Weight Statistics (Metric Units):", weight_stats)
print("Lifespan Statistics (Years):", lifespan_stats)
print("Country and Breed Frequency Table:")
print(country_breed_table)




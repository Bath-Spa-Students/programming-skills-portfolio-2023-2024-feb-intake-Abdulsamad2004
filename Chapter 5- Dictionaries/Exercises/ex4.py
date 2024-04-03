# Define the dictionary of rivers and countries
rivers = {
    "nile": "Egypt",
    "amazon": "Brazil",
    "mississippi": "United States"
}

# Print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.capitalize()} river runs through {country}.")

# Print the name of each river
print("\nRivers:")
for river in rivers.keys():
    print(river.capitalize())

# Print the name of each country
print("\nCountries:")
for country in rivers.values():
    print(country)

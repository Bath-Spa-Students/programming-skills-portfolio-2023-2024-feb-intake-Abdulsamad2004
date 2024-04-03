# Define dictionaries representing different pets
pet1 = {"kind": "dog", "owner": "Abdul Rehman"}
pet2 = {"kind": "cat", "owner": "Irtiza"}
pet3 = {"kind": "parrot", "owner": "Abdul Samad"}

# Store the dictionaries in a list called pets
pets = [pet1, pet2, pet3]

# Loop through the list of pets and print information about each pet
for pet in pets:
    print(f"Kind: {pet['kind'].capitalize()}")
    print(f"Owner: {pet['owner'].capitalize()}")
    print()  # Insert a blank line between each pet

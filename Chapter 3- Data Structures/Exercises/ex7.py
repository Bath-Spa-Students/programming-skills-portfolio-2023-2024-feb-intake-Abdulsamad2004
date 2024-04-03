# Define a list of places to visit
places_to_visit = ["Tokyo", "Paris", "Machu Picchu", "Santorini", "New York City"]

# Print the list in its original order
print("Original order:", places_to_visit)

# Print the list in alphabetical order using sorted()
print("Alphabetical order:", sorted(places_to_visit))

# Show that the original list is still in its original order
print("Original order after sorting:", places_to_visit)

# Print the list in reverse alphabetical order using sorted()
print("Reverse alphabetical order:", sorted(places_to_visit, reverse=True))

# Show that the original list is still in its original order
print("Original order after reverse sorting:", places_to_visit)

# Change the order of the list using reverse()
places_to_visit.reverse()
print("Reversed order:", places_to_visit)

# Change the order of the list again using reverse()
places_to_visit.reverse()
print("Back to original order:", places_to_visit)

# Change the order of the list using sort() to alphabetical order
places_to_visit.sort()
print("Alphabetical order using sort():", places_to_visit)

# Change the order of the list using sort() to reverse alphabetical order
places_to_visit.sort(reverse=True)
print

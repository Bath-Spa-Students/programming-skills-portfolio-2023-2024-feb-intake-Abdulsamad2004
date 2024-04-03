# Define a list of people to invite to dinner
guests = ["Taha", "Irtiza", "Fassi"]

# Print an invitation message to each person
for person in guests:
    print(f"Dear {person}, I would like to invite you to dinner. It would be an honor to have you join us.")

# Print a message saying only two people can be invited
print("\nSorry, but due to unforeseen circumstances, we can only invite two people for dinner.\n")

# Use pop() to remove guests until only two names remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, but we won't be able to accommodate you for dinner.")

# Print invitation messages to the two remaining guests
for person in guests:
    print(f"Dear {person}, you're still invited to dinner.")

# Use del to remove the last two names from the list
del guests[:]
print("\nCurrent guest list:", guests)

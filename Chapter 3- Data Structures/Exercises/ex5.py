# Define a list of people to invite to dinner
guests = ["Taha", "Irtiza", "Fassi"]

# Print an invitation message to each person
for person in guests:
    print(f"Dear {person}, I would like to invite you to dinner. It would be an honor to have you join us.")

# Print the name of the guest who can't make it
guest_cant_make_it = guests.pop(1)  # Assume Ada Lovelace can't make it
print(f"\nUnfortunately, {guest_cant_make_it} can't make it to dinner.\n")

# Add a new person to the list of guests
new_guest = "kamran"
guests.append(new_guest)

# Print a second set of invitation messages
for person in guests:
    print(f"Dear {person}, I would like to invite you to dinner. It would be an honor to have you join us.")

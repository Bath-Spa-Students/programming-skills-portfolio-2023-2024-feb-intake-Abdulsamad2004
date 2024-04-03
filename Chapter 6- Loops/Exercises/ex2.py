# Define ticket prices based on age
ticket_prices = {
    "under_3": 0,
    "3_to_12": 10,
    "over_12": 15
}

# Prompt users for their age until they enter 'quit'
while True:
    age_input = input("Please enter your age (or 'quit' to exit): ")
    
    # Check if the user wants to quit
    if age_input.lower() == 'quit':
        break
    
    # Convert age input to an integer
    try:
        age = int(age_input)
    except ValueError:
        print("Please enter a valid age.")
        continue
    
    # Determine the ticket price based on age
    if age < 3:
        ticket_price = ticket_prices["under_3"]
    elif age <= 12:
        ticket_price = ticket_prices["3_to_12"]
    else:
        ticket_price = ticket_prices["over_12"]
    
    # Print the cost of the movie ticket
    print(f"The cost of your movie ticket is ${ticket_price}.")

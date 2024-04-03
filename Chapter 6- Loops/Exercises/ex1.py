# Initialize an empty list to store pizza toppings
pizza_toppings = []

# Prompt the user to enter pizza toppings
while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    
    # Check if the user wants to quit
    if topping.lower() == 'quit':
        break
    
    # Add the topping to the list
    pizza_toppings.append(topping)
    
    # Print a message confirming the topping has been added
    print(f"Adding {topping} to your pizza.")

# Print the list of pizza toppings
print("Your pizza will have the following toppings:")
for topping in pizza_toppings:
    print("- " + topping)

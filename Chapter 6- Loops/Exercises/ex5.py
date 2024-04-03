# Make a list called sandwich_orders and fill it with sandwich names
sandwich_orders = ["pastrami", "tuna", "pastrami", "turkey", "pastrami", "chicken", "meat and cheese", "pastrami"]

# Make an empty list called finished_sandwiches
finished_sandwiches = []

# Print a message indicating the deli has run out of pastrami
print("Sorry for the inconveniance, the deli has run out of pastrami.")

# Remove all occurrences of 'pastrami' from sandwich_orders
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Loop through the list of sandwich orders
while sandwich_orders:
    # Take the first sandwich order from the list
    current_order = sandwich_orders.pop(0)
    
    # Print a message indicating the sandwich is being made
    print(f" your {current_order} sandwich is ready.")
    
    # Add the finished sandwich to the list of finished sandwiches
    finished_sandwiches.append(current_order)

# Print a message listing each sandwich that was made
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print("- " + sandwich.capitalize())

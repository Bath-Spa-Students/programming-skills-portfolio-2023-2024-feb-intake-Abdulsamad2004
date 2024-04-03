# Make a list called sandwich_orders and fill it with sandwich names
sandwich_orders = ["tuna", "turkey", "chicken", "meat and cheese"]

# Make an empty list called finished_sandwiches
finished_sandwiches = []

# Loop through the list of sandwich orders
while sandwich_orders:
    # Take the first sandwich order from the list
    current_order = sandwich_orders.pop(0)
    
    # Print a message indicating the sandwich is being made
    print(f"I made your {current_order} sandwich.")
    
    # Add the finished sandwich to the list of finished sandwiches
    finished_sandwiches.append(current_order)

# Print a message listing each sandwich that was made
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print("- " + sandwich.capitalize())

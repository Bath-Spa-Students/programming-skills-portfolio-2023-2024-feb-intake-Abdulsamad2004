def make_shirt(size, message):
    """Prints a sentence summarizing the size of the shirt and the message printed on it."""
    print(f"A {size} shirt will be made with the message: '{message}'.")

# Call the function once using positional arguments
make_shirt("medium", "GTR>>>>")

# Call the function a second time using keyword arguments
make_shirt(size="large", message="SUPRA>>>>>")

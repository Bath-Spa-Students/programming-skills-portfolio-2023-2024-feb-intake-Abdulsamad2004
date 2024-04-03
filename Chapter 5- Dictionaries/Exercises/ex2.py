# Define the glossary
glossary = {
    "variable": "A storage location in a program that holds a value.",
    "function": "A named sequence of statements that performs a specific task.",
    "loop": "A control flow statement for executing code repeatedly.",
    "list": "A collection of items that are ordered and changeable.",
    "dictionary": "A collection of key-value pairs that allows efficient lookup, insertion, and deletion of items."
}

# Print each word and its meaning
for word, meaning in glossary.items():
    print(word.capitalize() + ":", meaning)
    print()  # Insert a blank line between each word-meaning pair

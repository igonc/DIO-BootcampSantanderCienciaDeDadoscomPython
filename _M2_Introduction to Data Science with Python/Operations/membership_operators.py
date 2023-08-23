# Membership Operators in Python
print("Membership Operators in Python")

# Example 1: "in" operator with a list
fruits = ["apple", "banana", "cherry", "orange"]

print("\nExample 1:")
print("List of fruits:", fruits)
print("Is 'apple' in the list?", "apple" in fruits)  # True, because "apple" is in the list
print("Is 'grape' in the list?", "grape" in fruits)  # False, because "grape" is not in the list

print("In Example 1, the 'in' operator is used to check if 'apple' is present in the 'fruits' list (which it is), and it also checks if 'grape' is in the list (which it is not).")

# Example 2: "not in" operator with a tuple
colors = ("red", "green", "blue")

print("\nExample 2:")
print("Tuple of colors:", colors)
print("Is 'yellow' not in the tuple?", "yellow" not in colors)  # True, because "yellow" is not in the tuple
print("Is 'red' not in the tuple?", "red" not in colors)        # False, because "red" is in the tuple

print("In Example 2, the 'not in' operator is used to check if 'yellow' is not present in the 'colors' tuple (which it is not), and it checks if 'red' is not in the tuple (which it is).")

# Example 3: Membership with strings
text = "Hello, world!"

print("\nExample 3:")
print("Text string:", text)
print("Is 'Hello' in the text string?", "Hello" in text)        # True, because "Hello" is in the string
print("Is 'Python' not in the text string?", "Python" not in text)  # True, because "Python" is not in the string

print("In Example 3, membership operators are used with a string. It checks if 'Hello' is in the 'text' string (which it is) and if 'Python' is not in the string (which it is not).")

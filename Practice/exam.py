#2(A)
import random

# Define the universe of characters from which to choose
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# Generate 10 random 5-character strings using list comprehension
random_strings = [''.join(random.choice(chars) for _ in range(5)) for _ in range(10)]

# Print the list of random strings
print(random_strings)

#2(B)
def string_lengths(input_list):
    # Use list comprehension to generate a list of lengths of strings
    lengths = [len(string) for string in input_list]
    return lengths

# Example usage:
input_list = ["apple", "banana", "orange", "kiwi"]
result = string_lengths(input_list)
print(result)  # Output: [5, 6, 6, 4]

#3(A)


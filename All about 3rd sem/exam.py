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

#5(A)
for i in range(1,5+1):
    for j in range(1,i+1):
        print(i,"",end="")
    print()

#5(B(iv))
k=1
for i in range(1,5+1):
    for j in range(1, i+1):
        print(k,"", end="")
        k=k+1
    print()

#5(B(iii))
print(10/3) 
print(10//3)

#7(B(ii))
# Define an initial list
my_list = [1, 2, 3]

# Append a single element to the list
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
# Append elements of an iterable to the list
my_list.extend("dev")
print(my_list)  # Output: [1, 2, 3, 4, 5, 6, 7]

#7(B(iii))
# Define a list
my_list = [1, 2, 3, 4, 5]

# Convert the list to a tuple
my_tuple = tuple(my_list)

print(my_tuple)  # Output: (1, 2, 3, 4, 5)

#7(B(iv))
LL = ["Gfg", "is", "Good", "for"]
DD = {"Gfg": 5, "Best": 6}
K = "Gfg"

if K in LL and K in DD:
    value = DD[K]
    print(f"The value of '{K}' from the dictionary is: {value}")
else:
    print(f"The key '{K}' is not present in both the list and the dictionary.")

my_list = [1,"hi",True]
print (type(my_list))
print (my_list)

my_tuple = (1,"hi",True)
print (type(my_tuple))
print (my_tuple)

words = ["hello", "world", "python"]
uppercased_words = [word.upper() for word in words]  # Capitalize each word with list comprehension
joined_string = " ".join(uppercased_words)  # Join words into a string
print(joined_string)  # Output: HELLO WORLD PYTHON

string = "Why you are sad"
new = " ".join([s for s in string])
print(new)

numbers = [1, 2, 3, 4, 5]
squared_numbers = [num * num for num in numbers]  # Square each number
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

name_list = ["dev","mahadev","nilkantha","jatadari"]
name = input("Enter you name !")

if name in name_list:
  print("Naman hay, \"the altimate power\" ko")
else:
  print("You have to improve !")
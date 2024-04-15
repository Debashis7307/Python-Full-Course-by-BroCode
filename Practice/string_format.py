###### str.format() = optionam method that gives users more control when displaying output

animal = "cow"
item = "moon"
print("The {} jumped over the {} .".format(animal,item))  # useing variables name
print("The {} jumped over the {} .".format("boll","filder"))  # useing derict string
print("The {1} jumped over the {0} .".format("boll","filder"))  # useing indexing
print("The {u2} jumped over the {u2} .".format(u1="boll",u2="filder"))  # useing keywords in arguments

text = "I love {} as well as {} too ."
print(text.format("S","D"))

name = "Mahadev"
print("This is what {} you want to see".format(name))
print("This is what {:<10} you want to see".format(name)) # for right specess
print("This is what {:>10} you want to see".format(name)) # for left specess
print("This is what {:^10} you want to see".format(name)) # for middle 

number1 = 3.14159
number2 = 1000
print("The number pi is {:.2f}".format(number1))
print("The number is {:,}".format(number2))
print("The binary number is {:b}".format(number2))
print("The octal number is {:o}".format(number2))
print("The hexadesimal number is {:x}".format(number2))
print("The scintific number is {:E}".format(number2))

#Using f"string"
l="loru"
u="dkbose"
sen=f"Are vag na {l}, sunta ku nahi {u}..."
print(sen)
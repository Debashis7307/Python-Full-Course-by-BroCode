##########  writing my first program ########

print("Hey there, I am Debashis")
print('I am here to learn someting new...in the field of tech')

########## variables and data type  ##########

name = "Debashis" #string data type
print(type(name)) # type is used for checking the type of verible
name1 = "Bera"
print(name+" "+name1)
age = 20  #int datatype
age+=2
print("You are going to self dependent in the age of "+str(age))#this is called type casting
print(type(age))
hight=5.3 #float data type
print("My hight is : "+str(hight)+" feet")
print(type(hight))
mind= True #bool data type
print("I can do everything what I can think : "+str(mind))

###########  multiple assingment  #########

name, age,handsome="yatrik is not just a name",19,True
print(name,age,handsome)

######## useful String Methods ########

print(len(name))  # for the length of the string
print(name.find("k")) # find the charecter index no
print(name.capitalize()) # just capitalize the first letter of the string
print (name.upper())
print (name.lower())
print (name.isdigit())
print (name.isdecimal())
print (name.isalpha()) # to check wheather the string contains any space ro not!
print(name.count("a")) #to count how many 'a' are there
print(name.replace("yatrik","mahadev")) # to replece something to another thing
print(name*3 )

######## user input #######

name= input("What is your name? :")
age= int(input("How old are you? :"))
hight= float(input("What is your hight? :"))
print("Hello "+name+" , Welcome to my coding World!")
if(age>=18):
    print("You are allowed, as you are "+str(age)+" years old.")
else:
    print("You are not allowed, as your age is bellow 18.")

print("I know your hight is "+str(hight)+" cm.")
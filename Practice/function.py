#### function = is a  block of code which is executed only when it is called.

def hello(name,age):
    print("Hey! "+ name)
    print("Congrats , you are becomming  "+ age+" years in this year!")
    print("Have a nice day!")

name=input("Enter your name")
age=input("Enter your age")
hello(name,age)             ### we can pass arguments in the ()



### function return statements #####
def maltipal(num1,num2):
    return num1 * num2

x= int(input("Enter the number 1 : "))
y= int(input("Enter the number 2 : "))
z = maltipal(x,y)
print("The result is: ",str(z))




#### keywords arguments  ####
def hello2(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)

hello2(last="Bera",first="Alak",middle="Kumar")




#### nested function calls #####
print(round(abs(float(input("Enter a whole positive number:")))))




#### variables scope ####
name = "Mahadev"  #global variable
def display():
    name = "Dev"  #local variable
    print(name)
print(name)
display()




#### *args =  parameter that will pack all arguments into a tuple
            # it can accept a varying amount of arguments

def add(*args):
    sum=0
    for i in args:
        sum +=i
    return sum
print(add(1,2,3,4,5,6))




#####  **kwargs =  parameter that will pic all arguments into a dictionary

def hallo(**kwargs):  #you can name anything in the place of kwargs but ** is must...
    # print("Hello"+" "+kwargs["first"]+" "+kwargs["last"])
    print("Hello",end=" ")
    for key,val in kwargs.items():
        print(val,end=" ")
        

hallo(first="Dev",middle="Pandy",last="Das")
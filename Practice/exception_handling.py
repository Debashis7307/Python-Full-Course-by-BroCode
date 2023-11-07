###  exception = events detected during execution that interrupt tha flow of a progam

try:
    num = int(input("Enter a number to divide: "))
    deno = int(input("Enter a number to divide by : "))
    result = num/deno
  
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero ! idiot !")
except ValueError as e:
    print(e)
    print("You have to enter only number !")
except Exception as e:
    print(e)
    print("Something went wrong :(")
else:
      print(result)

finally:
    print("Mahadev")
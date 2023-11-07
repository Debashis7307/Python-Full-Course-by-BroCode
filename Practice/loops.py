# while loop = a block of code , that execute as long as it's condition remain true
#              Unlimited...
name = ""
while not(name == "mahadev"):
    name = input("enter your name: ")

print("Hello "+ name)

# for loop =  execute for limited amount of times

for i in range(10):
    print(i+1)

for i in range(1,101,10):
    print(i)

count =0
for i in "Dev Suv":
    print(i)
    count+=1
print("letter no is : "+ str(count-1))

# nested loops = one loop inside another loop
#              patern matching

row = int(input("Enter the no of rows.."))
columns = int(input("Enter the no of columns.."))
symbol = input("which symbol you want to print...")
for i in range(row):
    for j in range(columns):
        print(symbol, end="")
    print()

    #loop control statements=
    # break-used to terminate loop entirely
    # continue - skips to the next iteration of the loop
    # pass - does nothing acts as a placeholder

while True:
    name = input("Enter your name: ")
    if name != "":
        break

phone = "629-717-2118"
for i in phone:
    if i=="-":
        continue
    print(i, end= " ")

for i in range(1,21):
    if i==17:
        pass
    else:
        print(i)
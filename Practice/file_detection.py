import os

path = "C:\\Users\\DEBASHIS BERA\\OneDrive\\Desktop\\File.txt"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("This is a file")
    elif os.path.isdir(path):
        print("This is a directory!")
else:
    print("That location does not exists!")

###### Read a File  ######

try:
    with open("C:\\Users\\DEBASHIS BERA\\Desktop\\x.txt","r") as file:
        print(file.read())

except FileNotFoundError as e:
    print(e)
    print("That file was not found :(")


###### Write a File  ######
text = "Hey Everyone, I am \n Debashis\nHave a nice day "
with open("C:\\Users\\DEBASHIS BERA\\Desktop\\write.txt","a") as file:  # w = rewriteing
    file.write(text)                                                    # a = append in behind



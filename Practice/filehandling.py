fil = open("file.txt","r")
data = fil.read()
print(data)
count =0
for char in data :
    if(char.isdigit()):
        count=count+1

print(count)

p = open("file.txt", "a");
p.write(data+"\n"+str(count))
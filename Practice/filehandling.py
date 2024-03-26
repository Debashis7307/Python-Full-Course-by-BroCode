# data = open('mypy.txt','r')
# print(data.read())
# data.close()

# with open("exam.txt","w") as d:
#   d.write("Its exam time , so you should consentrate at studes!")

f = open("mypy.txt","r")
while(True):
  line = f.readline()
  print(line)
  if not line:
    break
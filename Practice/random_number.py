import random

x = random.randint(1,6)  # for taking int randomly
y = random.random()  # for taking float randomly
print(x)

myList = ['Rock','Paper','Seissors']
z = random.choice(myList)
print(z)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)
print(cards)
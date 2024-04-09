# list = used to store multiple items in a singal variable 

food = ["rice","eag","fruits","nonvage"]
print(food)
print(food[3])
food[3]="vage"

food.append("ice-cream")
food.insert(0,"water")
food.pop()
food.remove("water")
food.sort()
# food.clear()

for i in food:
    print(i) 

# 2D lists = a list of list

drinks = ["water","coffee","milk","cold-drinks"]
dinner = ["rooti","sabgi","chicken fry"]
dessert = ["ice-cream","cake"]
food = [drinks,dinner,dessert]
print(food)
print(food[2][0])


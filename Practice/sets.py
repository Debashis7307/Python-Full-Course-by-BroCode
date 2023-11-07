# set = collection which is unindexed . No duplicate values

lunch = {"rice","fish","dul","sabji"}
dinner = {"rice","eag","dul","sabji","vaja"}
lunch.add("raita")
# lunch.remove("sabji")
# lunch.update(dinner)
# today_food = lunch
for x in lunch:
    print(x)

print(lunch.difference(dinner))    # which is not common
print(dinner.difference(lunch))
print(dinner.intersection(lunch))   # which is common things between two sets
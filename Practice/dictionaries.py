# dictionaries  = A changeable, unordered collection of unique key

capitals = {"India":"New Delhi",
            "USA":"Washington DC",
            "China":"Beijing",
            "West Bengal":"Kolkata",
            "Russia":"Moscow"}
# print(capitals.get(input("Name ? ")))
# print(capitals[input("Name ? ")])
print(capitals.keys())
print(capitals.values())
capitals.update({'Germany':'Berline'})
capitals.update({'West Bengal':'Kalyani'})
capitals.pop("China")

for key,values in capitals.items():
    print(key," : ",values)

capitals.clear()


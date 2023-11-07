# tuple = collection which is ordered and unchangeable
#         used to group together related data

its_me = ("Dev",20,"male")
print(its_me.count("Dev"))
print(its_me.index("Dev"))

for i in its_me:
    print(i)

if "Dev" in its_me:
    print("Deb is here!")
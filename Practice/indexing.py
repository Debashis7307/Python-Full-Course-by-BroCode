######### indexing by giving some values under []  ##########

name="dev suv"
if(name[0].islower()):
    name=name.capitalize()
print(name)
f_name = name[:3].upper()
l_name = name[4:].upper()
print(f_name)
print(l_name)
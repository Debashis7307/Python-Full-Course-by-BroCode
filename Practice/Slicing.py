# slicing = creat a substring by extracting elements from another string
#            indexing[] or slice()
#            [start : stop : steps]
            
name = "Debashis Bera"
first_name = name[:name.find("B")]
last_name = name[name.find("B"):]
funkey_name = name[::3]
reversed_name = name[::-1] # to reverse the name
print(name)
print(first_name)
print(last_name)
print(funkey_name)
print(reversed_name)

website1= "https://google.com"
website2= "https://repleDev.com"
slice = slice(8,-4)  # slice(start, stop)
print(website1[slice])
print(website2[slice])
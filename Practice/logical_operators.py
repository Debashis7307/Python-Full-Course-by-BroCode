# logical operator -> and , or , not

tem = int(input("what is the temparature outside ?"))
if tem >= 0 and tem <= 30:
    print("The temparature is quit good today..")
    print("You can go outside..")
elif tem < 0 or tem > 30 :
    print("Temparature is bad today!")
    print("One should stay at home!")

# not  -> logical operator - flip false to true or from true to false
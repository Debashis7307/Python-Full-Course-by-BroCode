import numpy as np
import pandas as pd

dict1 = {
    "name":["Debashis","Rohit","Sudip","Parthib","Arnab","Achintya","Anish"],
    "roll":[1,2,3,4,5,6,7],
    "city":["Sabang","Simla","Puri","Medinipur","Kolkata","Alipurdure","Dimondherber"],
    "hobby":["exploring","army","gym","ocaml","web-dev","polity","gate"]
}
df = pd.DataFrame(dict1)  # make a dataFrame from this dictionary 
pd.to_csv('friends.csv')  # make a csv file from this data frame
pd.to_csv('friends.csv',index = False)  # make a csv file from this data frame without indexing

df.head(3)  # it will show 3 data value from the up 
df.tail(3)  # it will show 3 data value from the down 

df.describe()  #it will calculate the numerical values in the form of  {count , mean , std , min , 25% , 50% , 70% , max }
 
read = pd.read_csv('friends.csv')  # to read any exgisting csv file
df['name']  # to acess a perticular calumn
df['name'][4]  # to acess a perticular element
df['name'][4] = 'Mahadev'  # to change the perticular element

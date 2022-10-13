#dictionary car model
car={'name':'thar','colour':['black','red','blue'],'year':2022}


#access the dictionary items
print(car['year'])

#get method

print(car.get('name'))
#access key names
print(car.keys())

#adding new field

car['price range']=['20 lakh','18 lakh','16 lakh']
print(car.values())

print(car.items())

car['year']=2023
print(car)
#update element
car.update({'name':'range rover'})
print(car)

#remove dict items
car.pop('year')

car.popitem()
print(car)

#del

del car['colour']
print(car)

#clear
car.clear()
print(car)


#looping in dict

fruits={'name':'plum','quantity':20,'colour':'red','size':'small'}
#for i in fruits:
   # print(i,fruits[i])

#for i in fruits.keys():
   # print(i)

#for i,j in fruits.items():
    #print(i,j)


#1 copy a  dictionary

new=fruits.copy()
print(new)

#2 dict method

newvar=dict(fruits)
print(newvar)

#nested dictionaries----dict inside dict


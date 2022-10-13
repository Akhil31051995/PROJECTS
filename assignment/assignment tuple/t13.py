#Python – Remove Tuples from the List having every element as None

list=[(1,2),(None),(5,6,7),(99,52),(None),(None),('a','b')]
new=[]
for i in list:
    if i!=None:
        new.append(i)

print(new)


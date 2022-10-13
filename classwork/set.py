#sets
a={'apple',1,5,6,'mango','kiwi'}
b={1,2,3,6,8,'you','we'}
#print(set(b))   #convert to set set fn

#print(len(b))
#print(type(a))

#accessing set items

#for i in a:
 #   print(i)   #prints unordered in case of sets. doesnt allow duplicates.  can add or del items only .cannot modify

#add values
#a.add('orange')
#print(a)

#a.remove('mango')

#a.discard(1)   #will not raise error even if the element not present in set
#a.discard('cat')
#print(a)

#adding set ---use update fn

#a.update(b)
#print(a)

#c=['yellow','red','blue','green','pink']    #can add list or tuples to set using update fn
#a.update(c)
#print(a)


#joining sets

#union fn

c=a.union(b)
print(c)

#intersection   ----common elements finding

e={'a','c','h'}
f={'e','c','h','k'}
#d=e.intersection_update(f)

#symmetric difference update
d=e.symmetric_difference(f)           #prints elements other than common elements---common excluded
print(d)


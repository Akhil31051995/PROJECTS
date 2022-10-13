#Python program to interchange first and last elements in a list

new=['a','b','c','d','e','f','g','h']


first=new.pop(0)
last=new.pop(-1)
print(new)
new.insert(0,last)
print(new)
new.insert(len(new),first)  #why -1 position not working?
print(new)



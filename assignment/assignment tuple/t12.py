#Python – Remove Tuples of Length K

list=[('t1','t2','t3'),(1,2,3,4),('x','y','w','z'),(4,5,6),('c','k'),(0,1,7,9),('sea','hill'),('a','b')]
new=[]
n=int(input('enter the length of tuples to remove'))
for i in list:
    if len(i)!=n:
        new.append(i)

print(new)

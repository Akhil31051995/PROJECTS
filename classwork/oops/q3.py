# 9)sort the array 0s,1s and 2s
new=[]
a=[10,20,11,12,200,210,247]
for i in a:
    for j in str(i):
        if int(j)==0 or int(j)==1 or int(j)==2:

            new.append(int(j))



new.sort()
print(new)


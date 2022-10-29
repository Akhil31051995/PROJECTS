#Rearrange the array in alternating positive and negative items
neg=[]
pos=[]
new=[]
a=[40,-20,-87,80,7,-25,-4,9,23,2,-9]
for i in range(len(a)-1):
    # if a[i]>0 and a[i+1]<0:
    #     continue
    if a[i+1]<0 and a[i]>0 and a.index(a[i])%2!=0:
        a[i],a[i+1]=a[i+1],a[i]
        print(a)



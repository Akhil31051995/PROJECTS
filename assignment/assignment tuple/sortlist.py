a=[1,3,5,6,2,88,63,18]

for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]>=a[j]:
            a[i],a[j]=a[j],a[i]
print(a)
#write a program to find sum of digits of numbers from range 100 to 200.and append even sum to even list and odd sum to odd list

a=c=[]

for i in range (100,201):
    k=0
    for j in str(i):
        k=k+int(j)
    c.append(k)
print(c)





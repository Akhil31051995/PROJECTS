
prime=[]
for i in range(2,10):
    for j in range(1,i):
        if i%j==0 and i%1==0:
            prime.append(i)


print(prime)
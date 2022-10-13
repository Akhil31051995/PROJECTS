#Display Fibonacci series up to 10 terms

n=int(input('no of terms'))
a,b=0,1
i=0
if n<0:
    print('invalid')
elif n>=0:
    while i<n:
        c=a+b

        a=b
        b=c
        i=i+1
        print(a)




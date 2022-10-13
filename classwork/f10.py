#write a program to find lcm of  nos using fn
# lcm of two nos by formula

def lcm(x,y):
    if x<y and y%x==0:
        hcf=x
    elif x>y and x%y==0:
        hcf=y

    elif y%x!=0 or x%y!=0:
        z=abs(x-y)
        k = abs(min(x, y) - z)
        if x%z==0 and y%z==0:
            hcf=z
        elif k<z and x%k==0 and y%k==0:
            hcf=k
        elif k>z:
            hcf=z/2         # guess

    else:
        hcf=1

    lcm=(x*y)/hcf
    print('lcm :',lcm)


lcm(2,3)
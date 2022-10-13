# write a program to find factorial using recursion(functions)

num = int(input('enter the number'))


def fact(n):

    f=1
    for i in range(1,num+1):
        f=f*i
    print('factorial of number=',f)


fact(num)









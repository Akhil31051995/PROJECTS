#write a program to make simple calculator --mod ,floor div ,add,sub,multi,div (recursion)



def add():
    x = int(input('enter first no:'))
    y = int(input('enter second no: '))
    sum=x+y
    print('sum:',sum)

def difference():
    x = int(input('enter first no:'))
    y = int(input('enter second no: '))
    diff=x-y
    print('difference:',diff)

def product():
    x = int(input('enter first no:'))
    y = int(input('enter second no: '))
    product=x*y
    print('product:',product)

def div():
    x=int(input('number?:'))
    y=int(input('divisor:'))
    q=x/y
    print('quotient:',q)


def mod():
    x = int(input('number?:'))
    y = int(input('divisor: '))

    rem=x%y
    print('remainder:',rem)
def floor():
    x = int(input('number?:'))
    y = int(input('divisor: '))
    intq=x//y
    print('integer part of quotient :',intq)


add()
difference()
product()
div()
mod()
floor()

def name(a,b,c):
    print('the younger child name is',c)


#name(a='akhil',b='ram',c='tom')

#arbitrary keyword--**

def child(**args):
    print('name is:',args['lname'])

child(name='tom',lname='cruise',age=23)  #any no of arguments


#default parameter---

# def my_function(country= 'norway'):
#     print('i am from '+ country)
#
# my_function()
# my_function('india')

#passing list as argument

def foodlist(a):
    for x in a:
        print(x)

list=[1,2,3,4,5]

foodlist(list)

def mul(a):

    return (a*5)


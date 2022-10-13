#list
fruits=['apple','orange','banana','grapes','jack fruit','apple',1,2,3,True,False,True]
print(fruits[4])
print(fruits[6])
print(len(fruits))

a=list((1,2,3,'dog','cat'))
print(a)


#accessing list items

my_list=[1,2,'harry','tony','john']

print(my_list[-2])
print(my_list[2:6])
print(my_list[2:])
print(my_list[:3])
print(my_list[-4:-2])

if 'harry' in my_list:
    print('yes')
else:
    print('not found')

#change item value

my_list[0]='cherry'
print(my_list)

#change range of values
my_list[1:3]=['a','b']
print(my_list)

my_list[2:3]=['b1','b2','b3']

print(my_list)

#insert()

h=[1,2,3,4,5,6,7,8,9]
h.insert(2,'apple')
print(h)


#append()

h.append('mango')
print(h)

#extend - append elements from other list

h.extend(fruits)
print(h)

#remove list items

h.remove('grapes')
print(h)

#pop fuunction

h.pop(9)
print(h)

h.pop()
print(h)# last item removed by default

#del
#remove first item
del h[0]
print(h)




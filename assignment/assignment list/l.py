#tuple

fruits=('apple','mango','grapes','plum','banana')
print(type(fruits))
print(len(fruits))

#access the second last item in tuple

print(fruits[-2])

print(fruits[1:3])

#change first value and append element
b=list(fruits)
b[0]='a'
b.append('kiwi')
c=tuple(b)
print(c)

y=('papaya',) #one element tuple use comma
print(y)
c=c+y   #adding two tuples
print(c)



#i=0
#while i<len(c):
    #print(c[i])
   # i=i+1

#multiply a tuple
a=c*3
print(a)


#tuple methods
# count elements in a tuple   ----count function

for i in a:
    d=a.count(i)




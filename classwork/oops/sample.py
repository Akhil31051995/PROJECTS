# a={'a':1,'b':3,'c':5}
# def key(value):
#     for k,v in a.items():
#         if value==v:
#             return k
#
# print(key(3))

# a['c']=5
# print(a)
# d='a'
# print(d.islower())

# x=['akhi']
# y=['boy']
# print(x[0]+y[0])

# k='kalyani'
# print(k.index('l'))


s=[]
#s.extend(['none']*3)          #useful to add same item multiple times to list
s+=3*['none']                      #same use as above
print(s)



b=[1,2,3,4,5]
c=[1,3,5,7]
d=[1,20,3,4]

for i,j,k in zip(b,c,d):
    print(i,j,k)
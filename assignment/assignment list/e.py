#Python | Count occurrences of an element in a list

'''
a=['apple','mango','apple','mango','grapes','plum','grapes','apple','mango','mango','mango']
counta=countm=countg=countp=0
for i in a:
    if 'apple' in i:
        counta=counta+1
    if 'mango' in i:
        countm+=1
    if 'grapes' in i:
        countg+=1
    if 'plum' in i:
        countp+=1

print('apple=',counta)
print('mango=',countm)
print('grapes=',countg)
print('plum=', countp)
'''

b=[1,2,6,6,1,1,2,1,1,1,'apple','mango','apple','mango','grapes','plum']
counta=countm=countg=countp=count1=count2=count6=0
for i in b:
    if i=='apple':
        counta+=1
    if i=='mango':
        countm+=1
    if i=='grapes':
        countg+=1
    if i=='plum':
        countp+=1

    if i==1:
        count1+=1
    if i==2:
        count2+=1
    if i==6:
        count6+=1

print('count1',count1)
print('count2',count2)
print('count6',count6)
print('counta',counta)
print('countm',countm)
print('countg',countg)
print('countp',countp)





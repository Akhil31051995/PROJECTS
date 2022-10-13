#Python – Join Tuples if similar initial element,


p=[(1,2,3),(2,99),(1,56,45),(3,3),(1,74)]
q=[]
r=[]
q1=tuple()
for i in p:
    if i[0]==1:
        q.append(i)
    else:
        r.append(i)
print(q)
print(r)
for j in q:
    q1=q1+j
print(q1)




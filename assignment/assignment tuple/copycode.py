# pick first element and add problem
test_list=[(5,6,5),(5,7),(6,8),(6,10),(7,13,34)]
res=[]
x=[]
for i in test_list:
    if i[0] not in x:
        x.append(i[0])
for i in x:
    p=[]
    p.append(i)
    for j in test_list:
        if i==j[0]:
            p.append(j[1])
    res.append(p)

print(res)
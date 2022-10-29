value = dict(zip('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1, 53)))

sent = 'abCDe MESsi'
d1 = []
d2 = []
upindex=[]
lowindex=[]
c = sent.split()  # main list
d1.append(c[0])  # 1 st sub list
d2.append(c[-1])  # 2nd sublist

fullstring=d1[0]+d2[0]
sum1 = 0
sum2 = 0
for i in d1:
    for j in i:
        sum1 = sum1 + value[j]
for i in d2:
    for j in i:
        sum2 = sum2 + value[j]

print('sum1:',sum1,'sum2:',sum2)

if sum2 > sum1:
    newstring=d2[0]+d1[0]

######################################################
for index in range(len(fullstring)):
    if fullstring[index].isupper()==True:
        upindex.append(index)
    else:
        lowindex.append(index)
######################################################

print(fullstring)

for i in range(len(newstring)):
    for j in upindex:
        if i == j:
            print(newstring[i].upper(),end='')


    for j in lowindex:
        if i==j:
            print(newstring[i].lower(),end='')



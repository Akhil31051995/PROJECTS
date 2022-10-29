value = dict(zip('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1, 53)))

sent = 'aBC DeF'
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
    # c[0], c[-1] = c[-1], c[0]

for index in range(len(fullstring)):
    if fullstring[index].isupper()==True:
        upindex.append(index)
    else:
        lowindex.append(index)

# upindex.extend(['None']*2)         #aavasyamilla
# lowindex.extend(['None']*4)        #aavasyamilla
# print(lowindex)          #low aakendath aan low index
# print(upindex)
# print(newstring)

# for k in range(len(newstring)):
#
#     if k in upindex:
#
#         print(newstring[k].lower(),end='')

    # if k in lowindex:
    #     print(newstring[k].upper())
#
#print(newstring)
# print(upindex)
# print(lowindex)
print(fullstring)
#print(newstring)

for i in range(len(newstring)):
    for j in upindex:

        if i == j:
            print(newstring[i].upper(),end='')

    for j in lowindex:
        if i==j:
            print(newstring[i].lower(),end='')




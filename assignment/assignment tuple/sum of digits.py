#
#
# digitsum=[]
# evenlist=[]
# oddlist=[]
# for i in range(100,201):
#     a=i%10
#     b=int((i%100)/10)
#     c=int(i/100)
#     k=a+b+c
#     digitsum.append(k)
#     if k%2==0:
#         evenlist.append(i)
#     else:
#         oddlist.append(i)
# print(digitsum)
# print('even=',evenlist)
# print('odd=',oddlist)

tot=0
for i in range(100,200):
    dig=i%10
    tot=tot+dig
    i=i//10
    print(tot)
    if tot%2==0:



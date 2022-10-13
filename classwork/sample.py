a=['string','friends']
b=[]
for i in a:
    b.append(i.upper())
print(b)
    #print(i.upper())
# b=a.upper()
# print(b)




for word in words:
    for letter in upper:
        if letter in word:
            countup+=1

    for letter in lower:
        if letter in word:
            countlow+=1

print('upper:',countup,'lower:',countlow)







upper=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower=[]
for i in upper:
    lower.append(i.lower())
sentence=input('write the sentence:')
words=sentence.split()
countup=0
countlow=0
for word in words:
    for letter in word:

        if letter in upper:
            countup+=1

    for letter in word:
        if letter in lower:
            countlow+=1

print('upper:',countup,'lower:',countlow)



def net_amount():

    deposit=[]
    withdrawl=[]
    while True:
        d = input('deposit D:')           #int aakiyal preshnm
        w = input('withdrawl W:')

        if (d=='none' and w=='none') or (w=='none' and d=='none') :
            break


        else:
            deposit.append(int(d))
            withdrawl.append(int(w))

            net=sum(deposit)-sum(withdrawl)
    print('Net amount:',net)


net_amount()


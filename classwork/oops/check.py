value = dict(zip('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1, 53)))

sent = 'aBC DeF'
d1 = []
d2 = []
c = sent.split()  # main list
d1.append(c[0])  # 1 st sub list
d2.append(c[-1])  # 2nd sublist

################################################
def key(number):
    for k, v in value.items():
        if number == v:
            return k
##################################################333
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
    c[0], c[-1] = c[-1], c[0]


for word in c:
    for letter in word:
        if value.get(letter) <= 26:
            updateno = value.get(letter) + 26
            print(key(updateno), end='')

        else:
            updateno = value.get(letter) - 26

            print(key(updateno), end='')



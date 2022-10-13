# Find the weight of each strings in the input sentence according to the following condition.
#
#     a - z = 1 - 26
#     A - Z = 27 - 52
#
# Sort the strings according to its weight in the descending order and change the case of each character in the string as per the input strings.
#
# 1.Input  = aBC DeF
# Output = dEF AbC
#
# Explanation - Second string "DeF" has more weight than the string "aBC".
# so sorted string is "DeF aBC".
# Now change the case according to the input string,



value=dict(zip('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',range(1,53)))
new=value.copy()

sent = 'aBC DeF'
d1=[]
d2=[]
c=sent.split()      #main list
d1.append(c[0])     #1 st sub list
d2.append(c[-1])    #2nd sublist
# print(d1)
# print(d2)
################################################
def key(number):
    for k,v in value.items():
        if number==v:
            return k
##################################################333

sum1=0
sum2=0
for i in d1:
    for j in i:
        #print(value[j])
        sum1=sum1+value[j]
for i in d2:
    for j in i:
        #print(value[j])
        sum2=sum2+value[j]



if sum2>sum1:
    c[0],c[-1]=c[-1],c[0]
    newsent=c[0] +' '+ c[-1]
    #print(c or newsent)              not necessary already updated to c

for word in c:
    for letter in word:
        if value.get(letter)<=26:
            updateno=value.get(letter)+26
            #print(updateno)
            print(key(updateno),end='')

            #new[letter]=value.get(letter)+26


        else:

            updateno = value.get(letter) - 26
            #print(updateno)
            print(key(updateno),end='')

        #print(letter)


            #print(value.get(letter))

#print(new)









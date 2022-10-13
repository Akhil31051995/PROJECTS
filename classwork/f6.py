# Write a program that accepts a sentence and calculate the number of upper
# case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9


def letter_count():
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

    print('upper case:',countup,'lower case:',countlow)

letter_count()





def love_calculator():

    p1=input('enter first person in caps')
    p2=input('enter second person in caps')

    p=p1+p2
    print(p)
    t=['T','R','U','E']
    l=['L','O','V','E']
    counttrue=0
    countlove=0

    for i in p:
        if i in t:
            counttrue+=1

        if i in l:
            countlove+=1
    print('counttrue:',counttrue)
    print('countlove:',countlove)

    score=int(str(counttrue)+str(countlove))
    print(score)


    if score<10 or score>90:
        print(f'your score is {score},you go together like coke and mentos ')
    elif 40<score<50:
        print(f'your score is {score},you are alright together.')
    else:
        print(f'your score is {score} .')


love_calculator()



a='AKHILP'
for row in range(9):
    for col in range(11):

        if (row==0 and col%2==0 and col!=0 and col!=10) or (row==1 and (row-col)%4==0) or (row==2 and col==0) or (row==2 and col==10):
            print('*', end=' ')
        elif (row-col==3):

        elif (row+col==13):
            print('*',end=' ')

        else:
            print(' ',end=' ')

    print()

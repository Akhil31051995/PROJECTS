try:
    sum = 0
    while True:
        a=int(input('enter the number'))

        sum=sum+a
        print(sum)
        if sum>=15000:
            break

    print('haihai')
except ValueError:
    print('the input is not supported')

    print('hellohello')

finally:
    print('this program is over')

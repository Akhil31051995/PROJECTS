

choice=int(input('1.file writing 2. update'))
if choice==1:
    m="w"
elif choice==2:
    m="a"
else:
    print('invalid')

f=open("go.txt",mode=m)
while True:
    a=input('enter the line')
    f.writelines(a)
    f.writelines("\n")
    ch=input('do you want to continue Y/N')
    if ch=="N":
        break

f.close()



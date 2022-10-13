#generate a python list of all the even nos between 9and40

def even_list():
    new_list=[]
    for i in range(9,41):
        if i%2==0:
            new_list.append(i)
        else:
            continue
    print(new_list)


even_list()

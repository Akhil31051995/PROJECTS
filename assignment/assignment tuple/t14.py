# Sort a list of tuples by second Item

list1 = [(1, 2, 3), (99, 20, 3), (8, 5, 87), (1, 45), (7, 1, 8)]
new = []

for i in range(len(list1)):
    if list1[i][1]<list1[i-1][1]:
        list1[i-1],list1[i]=list1[i],list1[i-1]
print(list1)







    #print(list1[i][1])

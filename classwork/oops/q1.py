#find min and max element in an array
#arr={1,5,3,2} print in sorted order
# write program to reverse array
#find smallest and largest element in array

#create 3 arrays and find common element in these arrays
#rearrange array in alternative positive and neg items


arr1=[60,82,2,3,5,7,8,6,4,55,43]
min=print('min:',min(arr1))
max=print('max:',max(arr1))

arr={1,5,3,2}
li=list(arr)
li.sort()
arr=set(li)
print(arr)

#reverse array
a=[60,82,2,3,5,7,8,6,4,55,43]
a.reverse()
print(a)


#find common element in array
b=[1,2,3,4,5]
c=[1,3,5,7]
d=[1,20,3,4,5]

for i in b:
    if i in c and d:
        print(i)



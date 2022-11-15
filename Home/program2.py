# Example
# Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
# Output: [7, 0, 8]
# Explanation: 342 + 465 = 807.
#
# Example
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
# Example
# Input: l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]
# Output: [8, 9, 9, 9, 0, 0, 0, 1]

l1=[2,4,3]
l2=[5,6,4]

l1.reverse()
l2.reverse()

# a=str(l1)
# b=str(l2)

f=''
g=''
for i in l1:
    f=f+str(i)

num1=f
print(num1)
for j in l2:
    g=g+str(j)
num2=g
print(num2)
output=list(str(int(num1)+int(num2)))

output.reverse()
print(output)

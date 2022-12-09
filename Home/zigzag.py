# 6. Zigzag Conversion
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:
# Input: s = "A", numRows = 1
# Output: "A"


s='PAYPALISHIRING'
numrows=3
list=[[] for row in range(numrows)]
row=0
up=True
for i in s:
    list[row].append(i)
    if (row==0) or (row<numrows-1 and up):
        row+=1
        up=True

    else:
        row-=1
        up=False


print(list)






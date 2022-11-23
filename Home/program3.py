# Example 1:
# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

map={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
s = "MCMXCIV"
num=0
last=0
for i in  s[::-1]:
    if map[i]>=last:
        num+=map[i]
    else:
        num-=map[i]
    last=map[i]

print(num)





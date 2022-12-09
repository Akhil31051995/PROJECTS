# 5. Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.
# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:
# Input: s = "cbbd"
# Output: "bb"

                                                       #BRUTEFORCE SOLUTION

s='babad'
r=s[::-1]
c=[]
for i in range(len(s)):
    for j in range(len(s),1,-1):
        #print(s[i]+s[i+1:j])
        c.append(s[i]+s[i+1:j])

#print(c)
for k in c:
    if k==k[::-1] and len(k)>1:
        print(k)
    else:
        continue





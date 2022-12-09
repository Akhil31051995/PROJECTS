# 4. Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).
#
# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


a=[1,2,3]
b=[4,5,6]
c=a+b
c.sort()

if len(c)%2==0:
    median=(c[int((len(c)/2)-1)]+c[int(len(c)/2)])/2
else:
    median=(c[int(len(c)/2)])

print(median)
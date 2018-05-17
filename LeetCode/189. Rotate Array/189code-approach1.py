#https://leetcode.com/problems/rotate-array/description/
#LeetCode 189. Rotate Array

#author:peihan
#date: 05/17/2018

# 方法一，直接在列表末尾删除，在列表开头插入

nums = [1,2,3,4,5,6,7]
k = 3


for i in range(k):
	nums.insert(0, nums[-1])
	nums.pop()

print(nums)




'''
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
	        nums.insert(0, nums[-1])
	        nums.pop()
'''
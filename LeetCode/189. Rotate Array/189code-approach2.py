#https://leetcode.com/problems/rotate-array/description/
#LeetCode 189. Rotate Array

#author:peihan
#date: 05/17/2018

# 方法二,这个有bug，需要修改一下

nums = [1,2,3,4,5,6,7]
k = 3
nums =[-1]
k = 5
#nums =[-1,-100,3,99]
#k = 2

nums=[1,2]
k = 3

if len(nums) < 2 :
	nums = nums
	print(nums)
else:
	result = []

	d = len(nums) - k

	for i in range(d,len(nums)):
		result.append(nums[i])

	for i in range(0,d):
		result.append(nums[i])

	nums[:] = result
	print (nums)

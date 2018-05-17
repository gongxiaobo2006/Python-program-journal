#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

#LeetCode 27. Remove Element

#author:peihan
#date: 05/17/2018




nums = [3,2,2,3]
val = 3

result = []
for num in nums: 
	if num != val: 
		result.append(num)
	else:
		pass
nums[:]=result
print(nums)

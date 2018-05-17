#https://leetcode.com/problems/single-number/description/
#LeetCode 136. Single Number

#author:peihan
#date: 05/17/2018

#方法一：集合相减
#nums = [2,2,1]
nums = [4,1,2,1,2]

val = sorted(nums)
print(val)

pre_val = start_val = None
result=[]
i = 0

for number in val:
	cur_val = number
	if cur_val == pre_val: 
		result.append(cur_val)
	pre_val = cur_val

nums = set(nums)
result = set(result)
nums = list(nums-result)
out = nums[0]

print (out)

# 方法2： 求和可得，这方法太厉害了
'''out = sum(list(set(nums)))*2 - sum(nums)
print (out)'''
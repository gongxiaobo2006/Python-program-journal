#https://leetcode.com/problems/rotate-array/description/
#LeetCode 189. Rotate Array

#author:peihan
#date: 05/17/2018

# 方法三

nums = [1,2,3,4,5,6,7]
k = 3

#nums =[-1,-100,3,99]
#k = 2


if k:
    if len(nums) < k:
        k -= len(nums)
nums[:] = list(nums[-k:] + nums[:-k])
print(nums)



print(nums[:3])
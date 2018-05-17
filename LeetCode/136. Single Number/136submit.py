#https://leetcode.com/problems/single-number/description/
#LeetCode 136. Single Number

#author:peihan
#date: 05/17/2018


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val = sorted(nums)
        pre_val = start_val = None
        result=[]
        for number in val:
	        cur_val = number
	        if cur_val == pre_val: 
		        result.append(cur_val)
	        pre_val = cur_val

        nums = set(nums)
        result = set(result)
        nums = list(nums-result)
        out = nums[0]
        return out
        






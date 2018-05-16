#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

#LeetCode 26. Remove Duplicates from Sorted Array

#author:peihan
#date: 05/16/2018



class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev_num = None
        result = []
        for number in nums:
            cur_num = number
            if prev_num == cur_num: 
                pass
            elif prev_num != cur_num:
                result.append(cur_num)
                prev_num = cur_num
        nums[:] = result
        return len(nums)
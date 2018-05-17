#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

#LeetCode 27. Remove Element

#author:peihan
#date: 05/17/2018




class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        result = []
        for num in nums: 
            if num != val: 
                result.append(num)
            else:
                pass
        nums[:]=result
        return (len(nums))
#https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

#LeetCode 108. Convert Sorted Array to Binary Search Tree

#author:peihan
#date: 05/18/2018



class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

nums = [-10,-3,0,5,9]

class Solution:
	def sortedArrayToBST(self,nums):
		if nums == []:
			#print(None)
			return None
		
		print(nums)
		mid_num = len(nums)//2
		print(mid_num)
		root = TreeNode(nums[mid_num])
		root.left = self.sortedArrayToBST(nums[:mid_num])
		root.right = self.sortedArrayToBST(nums[mid_num+1:])
		return root

test = Solution()
test.sortedArrayToBST(nums)
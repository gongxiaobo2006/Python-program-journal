#https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

#LeetCode 104. Maximum Depth of Binary Tree

#author:peihan
#date: 05/16/2018

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1
print(node.right)
#https://leetcode.com/problems/binary-tree-pruning/description/
#LeetCode 814. Binary Tree Pruning

#author:peihan
#date: 05/16/2018

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

Tree = TreeNode([1,None,0,0,1])
root = Tree

class Solution_recursive:
	def pruneTree(self, root):
		if root is None:
			return None
		root.left = self.pruneTree(root.left)
		root.right = self.pruneTree(root.right)

		if root.val == 0 and not root.left and not root.right:
			root = None

		return root


sol = Solution_recursive()
print (sol.pruneTree(root))

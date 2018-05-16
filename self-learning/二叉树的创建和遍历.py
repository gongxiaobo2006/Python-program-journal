

'''# Test Tree example 1
G = ['G', [] ]
H = ['H', [] ]
I = ['I', [] ]
K = ['K', [] ]
E = ['E', [G,H,I,K]]
D = ['D', [] ]
F = ['F', [] ]
A = ['A', [D,E]]
B = ['B', []]
C = ['C', [F]]
Root = ['Root',[A,B,C]]
print (Root)
'''

#Test tree example 2 - binary tree 
class BTree:
	def __init__(self, value):
		self.data = value
		self.left = None
		self.right = None
	def insertLeft(self,value):
		self.left = BTree(value)
		return self.left
	def insertRight(self,value):
		self.right = BTree(value)
		return self.right
	def show(self):
		print(self.data)

if __name__ == '__main__':
	Root = BTree('Root')
	A = Root.insertLeft('A')
	C = A.insertLeft('C')
	D = A.insertRight('D')
	F = D.insertLeft('F')
	G = D.insertRight('G')
	B = Root.insertRight('B')
	E = B.insertRight('E')
	#Root.show()
	#Root.left.show()
	#Root.right.show()
	#A = Root.left
	#A.left.show()
	#Root.left.right.show()



def preorder(node): #前序遍历二叉树， 输出 root，左子树，再是右子树
	if node.data: 
		node.show()
		if node.left:
			preorder(node.left)
		if node.right:
			preorder(node.right)
print("前序遍历二叉树")
preorder(Root)
print("   ")
print("   ")

def medorder(node): #中序遍历二叉树， 输出左子树，root，再是右子树
	if node.data: 
		if node.left:
			medorder(node.left)
		node.show()
		if node.right:
			medorder(node.right)
print("中序遍历二叉树")
medorder(Root)
print("   ")
print("   ")

def backorder(node): #中序遍历二叉树， 输出左子树，root，再是右子树
	if node.data: 
		if node.left:
			backorder(node.left)
		if node.right:
			backorder(node.right)
		node.show()
print("后序遍历二叉树")
backorder(Root)











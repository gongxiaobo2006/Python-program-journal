
#https://leetcode.com/problems/flipping-an-image/description/
#LeetCode 832. Flipping an Image

#author:peihan
#date: 05/15/2018

#Input = [[1,1,0],[1,0,1],[0,0,0]] #test example1
Input=[[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]] #test example2
print(Input)
# step1: reverse the row of the matrix 
for i in range(len(Input)):
	Input[i].reverse()
print(Input)
#step2: change 1 to 0, and change 0 to 1
for i in range(len(Input)):
	for j in range(len(Input[0])):
		if Input[i][j] == 1:
			Input[i][j] = 0
		elif Input[i][j] == 0:
			Input[i][j] = 1
print(Input)
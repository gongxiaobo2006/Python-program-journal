
#https://leetcode.com/problems/flipping-an-image/description/
#LeetCode 832. Flipping an Image

#author:peihan
#date: 05/15/2018

class Solution:
    def flipAndInvertImage(self, A):
        Input = A
        # step1: reverse the row of the matrix 
        for i in range(len(Input)):
            Input[i].reverse()
        
        #step2: change 1 to 0, and change 0 to 1
        for i in range(len(Input)):
            for j in range(len(Input[0])):
                if Input[i][j] == 1:
                    Input[i][j] = 0
                elif Input[i][j] == 0:
                    Input[i][j] = 1
        Output = Input
        return Output
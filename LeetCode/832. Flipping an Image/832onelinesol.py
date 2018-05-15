#https://leetcode.com/problems/flipping-an-image/description/
#LeetCode 832. Flipping an Image

#author:peihan
#date: 05/15/2018


class Solution:
    def flipAndInvertImage(self,A):
        result = []
        for row in A:
            flippedRow = reversed(row)
            result.append(list(map(lambda x:1-a, flippedRow)))
        return result






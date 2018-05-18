#https://leetcode.com/problems/unique-paths/description/

#LeetCode 62. Unique Paths

#author:peihan
#date: 05/18/2018

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for col in range(m)]for row in range(n)]
        for col in range(m): 
	        for row in range(n):
		        if col == 0 and row == 0:
			        dp[row][col] = 1
		        elif col == 0 and row != 0:
			        dp[row][col] = dp[row-1][col]
		        elif col != 0 and row == 0:
			        dp[row][col] = dp[row][col-1]
		        else:
			        dp[row][col] = dp[row][col-1]+dp[row-1][col]
        
        return dp[-1][-1]
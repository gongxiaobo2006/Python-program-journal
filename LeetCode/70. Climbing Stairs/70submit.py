#https://leetcode.com/problems/climbing-stairs/description/
#LeetCode 70. Climbing Stairs

#author:peihan
#date: 05/17/2018

#方法；动态规划
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for col in range(n)]
        seq_1 = 1
        seq_2 = 0
        for i in range(n):
	        if i < 1:
		        dp[i] = seq_1 + seq_2
	        elif i == 1:
		        dp[i] = dp[i-1] + seq_1
	        else : 
		        dp[i] = dp[i-1] + dp[i-2] 
        
        return dp[-1]
        
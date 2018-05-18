#https://leetcode.com/problems/unique-paths/description/

#LeetCode 62. Unique Paths

#author:peihan
#date: 05/18/2018


#m = 3
#n = 2

m = 7
n = 3


dp = [[0 for col in range(m)]for row in range(n)]#生成dynamic programming矩阵
print(dp)
#dp[0][1] = 1
#print (dp) 

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


print (dp)
print (dp[-1][-1])
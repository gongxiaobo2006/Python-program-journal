#https://leetcode.com/problems/max-area-of-island/description/
#LeetCode 695. Max Area of Island

#author:peihan
#date: 05/15/2018



class Solution:
    def maxAreaOfIsland(self, grid):
        rows, cols = len(grid), len(grid[0])
        def dfs(i, j):
            if 0 <= i < rows and 0 <= j < cols and grid[i][j]: # grid[i][j]表示当前位置上有值 
                grid[i][j] = 0
                return 1 + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1)
            return 0
        
        result = 0
        for x in range(rows):
            for y in range(cols):
                if grid[x][y]: # grid[x][y]表示当前位置上有值 
                    result = max(result, dfs(x, y))   
        return result
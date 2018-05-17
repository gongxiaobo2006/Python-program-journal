
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

#LeetCode 122. Best Time to Buy and Sell Stock II

#author:peihan
#date: 05/17/2018




class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        if(len(prices)<2):
	        return 0
        else:
            start_val = pre_val = prices[0]
            for i in range(len(prices)):
	            cur_val = prices[i]
	            #print("之前的价格 ",pre_val,"  当前价格",cur_val," 收益",profit)
	            if cur_val < pre_val: 
		            profit = pre_val - start_val + profit
		            start_val = cur_val
	            pre_val = prices[i]
            profit = pre_val - start_val + profit
        
        return profit
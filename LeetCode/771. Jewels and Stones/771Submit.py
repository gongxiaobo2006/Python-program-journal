#https://leetcode.com/problems/jewels-and-stones/description/
#LeetCode 771. Jewels and Stones problems

#author:peihan
#date: 05/15/2018

class Solution:
    def numJewelsInStones(self, J, S):
        Jewels = list(J)
        Stones = list(S)
        count = 0 
        for Jew in Jewels:
	        for item in Stones:
		        if Jew == item:
			        count = count +1
		        else: 
			        pass
        return count
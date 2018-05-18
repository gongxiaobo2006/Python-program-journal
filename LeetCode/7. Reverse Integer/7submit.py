#https://leetcode.com/problems/reverse-integer/description/

#LeetCode 7. Reverse Integer

#author:peihan
#date: 05/18/2018

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = int(str(abs(x))[::-1])
        if num >= math.pow(2,31):
            return 0
        else:
            if x>0:
                return num
            else:
                return -num
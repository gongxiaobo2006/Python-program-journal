#https://leetcode.com/problems/reverse-string/description/

#LeetCode 344. Reverse String

#author:peihan
#date: 05/18/2018

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        lis_s = list(s)
        lis_s.reverse()
        string_s = ''.join(lis_s)
        return string_s
        
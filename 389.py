class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sum1=0
        sum2=0
        for i in s:
            sum1 += ord(i)
        for i in t:
            sum2 += ord(i)
        return chr(sum2-sum1)

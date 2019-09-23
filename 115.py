class Solution(object):
    def numDistinct(self, s, t):2
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp=[ [0 for _ in range(len(s))] for _ in range(len(t))]


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        res=0
        flag=0
        if x<0:
            flag=-11
        while x:
            left=x%10
            x=x/10
            res=res*10+left
        return res*flag

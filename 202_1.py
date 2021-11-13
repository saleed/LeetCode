class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        vis = set()
        vis.add(n)
        while True:
            s=0
            while n:
                s+=(n%10)*(n%10)
                n/=10
            if s in vis:
                return False
            else:
                vis.add(s)
                n=s
a=Solution()
print(a.isHappy(2))
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        p=n
        s=set()
        while p!=1:
            newp=0
            if p in s:
                return False
            else:
                s.add(p)
            while p!=0:
                newp+=(p%10)**2
                p/=10
            p=newp
        return True
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        p=n
        while p>0:
            bit=p&1
            p=p>>1
            if bit==1:
                if p==0:
                    return True
                else:
                    return False


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """

        sqc=math.sqrt(c)
        p=1
        q=sqc-1
        while p<=q:
            target=math.pow(2,p)+math.pow(2,q)
            if target==c:
                return True
            elif target<c:
                p+=1
            else:
                q-=1
        return False



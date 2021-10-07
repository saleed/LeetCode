class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x=str(x)
        p=0
        q=len(x)-1
        while p<q:
            if x[p]==x[q]:
                p+=1
                q-=1
            else:
                return False

        return True

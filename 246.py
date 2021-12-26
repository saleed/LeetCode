class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """

        p=0
        q=len(num)-1
        while p<q:
            if num[p]==num[q]:
                p+=1
                q-=1
            else:
                return False

        return True
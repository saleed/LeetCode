# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        p=1
        q=n
        while True:
            mid=(p+q)/2
            ret= guess(mid)
            if ret==0:
                return mid
            elif ret==1:
                p=mid+1
            else:
                q=mid-1
        



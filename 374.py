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
        s=0
        e=n
        count=0
        while guess((s+e)/2)!=0:
            if guess((s+e)/2)==-1:
                s=(s+e)/2+1# be careful for this
            else:
                e=(s+e)/2
            count+=1
        return count







# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left,right=1,n
        while left<right:
            mid=(left+right)/2
            if isBadVersion(mid)==False:
                left=mid+1
            else:
                right=mid  ###notice that binay search we can use the mid as right bound but we must use mid+1 as left bound because the (left+right)/2 give us low bound valuse
        return left


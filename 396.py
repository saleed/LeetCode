class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        maxsum = 0

        sumA=sum(A)
        weightsum=0
        for i in range(len(A)):
            weightsum+=i*(A[i])
        for i in list(reversed(A)):
            maxsum=max(maxsum,weightsum)
            weightsum=weightsum+sumA-len(A)*i

        return maxsum
A = [4, 3, 2, 6]
a=Solution()
print a.maxRotateFunction(A)
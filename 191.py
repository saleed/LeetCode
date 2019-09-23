class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        for i in range(32):
            if (n&pow(2,i))>>i==1: # must have bracket around n&pow(2,i) and be carful for the >>i operation
                count+=1
        return count

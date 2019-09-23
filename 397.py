class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        while n!=1:
            while n%2==1:
                n/=2
                count+=1
            if count==1:
                return count
            n-=1
            count+=1
            return count


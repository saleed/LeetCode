class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return 0
        a=[0]*len(n)
        count=0
        for i in range(2,n):
            if a[i]==0:
                count+=1
                j=2
                while j*i<n:
                    a[j*i]=1
            else:
                continue
        return count

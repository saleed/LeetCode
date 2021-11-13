class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=[1]*(n+1)
        i=2
        cnt=0
        while i<n:
            if l[i]==1:
                cnt+=1
                m=2
                while m*i<n:

                    l[m*i]=0
                    m+=1
            i+=1
        # print(l)
        return cnt

a=Solution()
print(a.countPrimes(10))







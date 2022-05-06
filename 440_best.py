class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        #
        # l=0
        # nn=n
        # while nn>0:
        #     l+=1
        #     nn/=10
        # res=""
        # for i in range(l):
        #     start=0
        #     if i==0:
        #         start=1
        #     fac=self.fac(l-1-i)
        #     while start*fac<k:
        #         start+=1
        #     res+=str(start-1)
        #     k=k-(start-1)*fac


    def fac(self,i):
        res=1
        for i in range(i):
            res*=i+1
        return res


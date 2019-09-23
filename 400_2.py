class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        preTotalNum=0
        nbit=0
        while preTotalNum<n:
            nbit+=1
            preTotalNum+=self.getNumOfDigitWithNbit(nbit)

        preTotalNum-=self.getNumOfDigitWithNbit(nbit)

        D=int((n-preTotalNum)/nbit)+max(1,(nbit-1)*10)
        print("###",D)
        div=max(1,(nbit-1)*10)
        left=(n-preTotalNum)%nbit
        res=-1
        while left>=0:
            res=int(D/div)
            D=D%div
            div/=10
            left-=1
        return res


    def getNumOfDigitWithNbit(self,n):
        res=1
        p=1
        while p<=n:
            if p==1:
                res=9
            else:
                res*=10
            p+=1
        print(res)
        return res





a=Solution()
print(a.findNthDigit(16))


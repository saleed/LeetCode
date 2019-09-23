class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum=0
        while n:
            sum+=int(n/5)
            n=int(n/5)
        return sum
        # 分别求5，25，125.。。的倍数





    def forcedSearch(self,):
        l1=0
        l2=0
        for i in range(1,n+1):
            c1,c2=self.twoandfivein(i)
            l1+=c1
            l2+=c2
        return min(l1,l2)


    def twoandfivein(self,n):
        p=n
        c1=0
        while p%2==0:
            p=p/2
            c1+=1
        p=n
        c2=0
        while p%5==0:
            p/=5
            c2+=1
        return c1,c2




   #求5的银子个数，仍然超时！！！！
    def twoin(self,n,ele):
        count=0
        p=1
        while pow(ele,p)<=n:
            i=1
            while i*pow(ele,p)<=n:
                # print(i*pow(ele,p))
                count+=1
                i+=1
            p+=1
        return count

        # return self.twoin(n, 5)






a=Solution()
print(a.trailingZeroes(1808548329))

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        return 0 if n == 0 else n / 5 + self.trailingZeroes(n / 5)



        dict={2:0,5:0}

        # dict[2]+=self.getDiv(n,2)
        dict[5]+=self.getDiv(n,5)
        return dict[5]





    def getDiv(self,n,divide):
        div=divide
        count=0
        while div<=n:
            c=1
            mul=div
            while mul<=n:  #this is actually divide
                count+=1
                c += 1
                mul=div*c
            div*=divide
        return count


a=Solution()
print a.getDiv(8,2)
# print a.getDiv(1808548329,2)
print 1808548329/2
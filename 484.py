class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        res=[i for i in range(1,len(s)+2)]
        i=0
        while i<len(s):
            if s[i]=="I":
                i+=1
            else:
                p=i
                while i<len(s) and s[i]=="D":
                    i+=1
                m=p
                n=i
                print(res,m,n)
                while m<n:
                    res[m],res[n]=res[n],res[m]
                    m+=1
                    n-=1
        print(res)
        return res


ss=Solution()
s="DI"
ss.findPermutation(s)



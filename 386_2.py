class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res=[]
        self.dfs("",n,res)
        print(res)
        return res









    def dfs(self,cur,n,res):
        if cur=="":
            val=0
        else:
            val=int(cur)
        if val<=n:
            if val!=0:
                res.append(cur[:])
            for i in range(10):
                if len(cur)==0 and i==0:
                    continue
                self.dfs(cur+str(i),n,res)



a=Solution()
print(a.lexicalOrder(13))
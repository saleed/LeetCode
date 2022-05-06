class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res=[]
        self.dfs(0,res,n)
        return res[1:]





    def dfs(self,cur,res,n):
        if cur<=n:
            res.append(cur)
            for i in range(10):
                if cur==0 and i==0:
                    continue
                newcur=cur*10+i
                self.dfs(newcur,res,n)




class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs(1,n,k,[],res)
        return res



    def dfs(self,id,n,k,cur,res):
        if k==0:
            res.append(cur[:])
            return
        if id<=n:
            self.dfs(id+1,n,k,cur,res)
            cur.append(id)
            self.dfs(id+1,n,k-1,cur,res)
            cur.pop()
        return
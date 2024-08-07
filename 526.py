class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rt
        ype: int
        """
        res=[0]
        self.dfs(n,n,set(),res)
        return res[0]

    def dfs(self,n,i,vis,res):
        if i==0:
            res[0]+=1
            return
        for j in range(1,n+1):
            if j not in vis and (j%i==0 or i%j==0):
                vis.add(j)
                self.dfs(n,i-1,vis,res)
                vis.remove(j)


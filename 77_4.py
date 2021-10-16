class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

    def dfs(self,i,left,n,res,cur):
        if left==0:
            res.append(cur[:])
        if i<=n:
            self.dfs(i+1,left,n,res,cur)
            cur.append(str(i))
            self.dfs(i+1,left-1,res,cur)

            ####注意这里可以使用pop()
            cur.pop()




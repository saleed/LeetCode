class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        res=[]
        s=[i+1 for i in range(10)]
        self.dfs2(k,n,0,s,[],res)
        print(res)
        return res

    def dfs2(self,k,left,id,s,cur,res):
        if left==0 and k==0:
            res.append(cur[:])
            return
        if left>0 and k>0 and id<len(s):
            self.dfs2(k,left,id+1,s,cur,res)
            cur.append(s[id])
            self.dfs2(k-1,left-s[id],id+1,s,cur,res)
            cur.pop()



k=3
n=7
a=Solution()
a.combinationSum3(k,n)
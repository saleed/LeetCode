class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        cursel=[]
        res=[]
        self.dfs(k,n,cursel,res,1)
        print(res)
        return res

    def dfs(self,k,left,cursel,res,n):
        print(k,left)
        if k==0 and left==0:
            # print cursel
            res.append(cursel[:])
        if k>0 and left>0:
            if n>9:
                return
            self.dfs(k,left,cursel,res,n+1)
            newsel=cursel[:]
            newsel.append(n)
            self.dfs(k-1,left-n,newsel,res,n+1)
        return


k=3
n=7
a=Solution()
a.combinationSum3(k,n)
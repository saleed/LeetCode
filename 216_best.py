class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        res=[]
        self.dfs(res,[],0,1,n,k)
        return res


    def dfs(self,res,tmp,tmpsum,i,target,k):
        if tmpsum==target:
            res.append(tmp[:])
            return
        if tmpsum<target and i<10 and k>0:
            self.dfs(res,tmp,tmpsum,i+1,target,k)
            tmp.append(i)
            self.dfs(res,tmp,tmpsum+i,i+1,target,k-1)
            tmp.pop()



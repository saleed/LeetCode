class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res=[]
        arr=[i+1  for i in range(n)]
        self.dfs(0,k,arr,[],res)
        return res


    def dfs(self,i,k,arr,tmp,res):
        if k==0:
            res.append(tmp[:])
            return
        if i<len(arr):
            self.dfs(i+1,arr,tmp,res)
            tmp.append(arr[i])
            self.dfs(i+1,arr,tmp,res)
            tmp.pop()


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs(k,n,0,[],res,1)
        return res





    def dfs(self,k,n,tmpsum,tmpsel,res,i):

        if tmpsum==k and len(tmpsel)==n:

        # if tmpsum == k :
            print(tmpsel, tmpsum)
            res.append(tmpsel[:])
            return
        if tmpsum<k and i<=9 and len(tmpsel)<n:
            self.dfs(k,n,tmpsum,tmpsel,res,i+1)
            tmpsel.append(i)
            self.dfs(k,n,tmpsum+i,tmpsel,res,i+1)
            tmpsel.pop()

k=7
n=3
a=Solution()
print(a.combinationSum3(k,n))
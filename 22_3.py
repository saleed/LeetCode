class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        self.dfs(0,0,"",res,n)
        return res





    def dfs(self,left,right,cur,res,k):
        if left==k and right==k:
            res.append(cur[:])
        elif right==left:
            cur+='('
            self.dfs(left+1,right,cur,res,k)
        elif left==k:
            cur+=')'
            self.dfs(left,right+1,cur,res,k)
        else:
            cur+='('
            self.dfs(left+1,right,cur,res,k)
            cur=cur[:-1]
            cur+=')'
            self.dfs(left,right+1,cur,res,k)
        return


a=Solution()
print(a.generateParenthesis(3))









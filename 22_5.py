class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        self.dfs(res,"",0,0,n)
        return res


    def dfs(self,res,tmp,nl,nr,n):
        if nl==n and nr==n:  ##最终结果
            res.append(tmp)
        elif nr==nl:  ##
            tmp+="("
            self.dfs(res,tmp,nl+1,nr,n)
        elif nl==n:
            self.dfs(res,tmp+")",nl,nr+1,n)
        else:
            self.dfs(res,tmp+"(",nl+1,nr,n)
            self.dfs(res,tmp+")",nl,nr+1,n)
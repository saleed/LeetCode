class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        self.dfs(0,0,n,"",res)
        return res



    def dfs(self,lnum,rnum,n,cur,res):
        if len(cur)==2*n:
            res.append(cur)
            return
        if lnum==rnum and lnum<n:
            newcur=cur+"("
            self.dfs(lnum+1,rnum,n,newcur,res)
        elif lnum>rnum:
            if lnum<n:
                newcur=cur+"("
                self.dfs(lnum+1,rnum,n,newcur,res)
            newcur=cur+")"
            self.dfs(lnum,rnum+1,n,newcur,res)


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        self.dfs(0,0,res,n,"")
        return res



    def dfs(self,lnum,rnum,res,n,tmp):
        print(lnum,rnum)
        if lnum==rnum and lnum==n:
            res.append(tmp)
            return
        elif lnum==n:
            tmp+=")"
            self.dfs(lnum,rnum+1,res,n,tmp)
        elif lnum==rnum:
            tmp+="("
            self.dfs(lnum+1,rnum,res,n,tmp)
        else:
            tmp+="("
            self.dfs(lnum+1,rnum,res,n,tmp)
            tmp=tmp[:-1]
            tmp+=")"
            self.dfs(lnum,rnum+1,res,n,tmp)


a=Solution()
n=3
print(a.generateParenthesis(3))

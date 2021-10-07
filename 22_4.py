class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        self.dfs(0,0,3,res,"")
        return res



    def dfs(self,left,right,n,res,tmp_res):
        if left==n and right==n:
            res.append(tmp_res[:])
            return
        if left==right:
            tmp_res+="("
            self.dfs(left+1,right,n,res,tmp_res)
        elif left>right:
            if left<n:
                tmp_res+="("
                self.dfs(left+1,right,n,res,tmp_res)
                tmp_res=tmp_res[:-1]
            tmp_res+=")"
            self.dfs(left,right+1,n,res,tmp_res)



if __name__=="__main__":
    a=Solution()
    print(a.generateParenthesis(3))

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits=="":
            return []

        dict={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        res=[]
        cur=""
        self.dfs(res,cur,digits,dict)
        return res



    def dfs(self,res,cur,digit,dict):
        if len(digit)==0:
            res.append(cur[:])
            return
        d=int(digit[0])
        for s in dict[d]:
            cur+=s
            self.dfs(res,cur,digit[1:],dict)
            cur=cur[:-1]

a=Solution()

print(a.letterCombinations("234"))

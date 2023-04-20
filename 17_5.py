class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d2sMap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}



        res=[]
        self.dfs(d2sMap,res,"",digits,0)
        return res


    def dfs(self,vdict,res,tmp,digits,i):
        if i==len(digits):
            res.append(tmp)
            return
        if digits[i] not in vdict:
            return 
        for l in vdict[digits[i]]:
            self.dfs(vdict,res,tmp+l,digits,i+1)

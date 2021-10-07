class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        d2sMap={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res=[]
        self.dfs(digits,res,"",d2sMap)
        return res



    def dfs(self,digit,res,tmp_res,d2sMap):
        if len(digit)==0 and len(tmp_res)>0:
            res.append(tmp_res[:])
            return
        if len(digit)>0:
            tmp_ch=digit[0]
            if tmp_ch not in d2sMap.keys():
                return
            chMap=d2sMap[tmp_ch]
            for ch in chMap:
                tmp_res+=ch
                self.dfs(digit[1:],res,tmp_res,d2sMap)
                tmp_res=tmp_res[:-1]




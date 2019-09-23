class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits=="":
            return []

        dict={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        # res=self.dfs(digits,dict)
        # strres=[]
        # for l in res:
        #     strres.append("".join(l))
        # return strres


        res=[]
        cur=""
        self.dfs2(digits,cur,res,dict)
        return res





    #不同方式的递归
    def dfs(self,digits,dict):
        if len(digits)==1:
            return list(dict[int(digits[0])])
        nexrec=self.dfs(digits[1:],dict)
        res=[]
        for i in range(len(dict[int(digits[0])])):
            for ele in nexrec:
                tmp=[dict[int(digits[0])][i]]
                tmp.extend(ele)
                res.append(tmp)
        return res

    def dfs2(self,digits,cur,res,dict):
        if len(digits)==0:
            res.append(cur[:])
            return
        d=int(digits[0])
        for i in range(len(dict[d])):
            cur+=dict[d][i]
            self.dfs2(digits[1:],cur,res,dict)
            cur=cur[:-1]



a=Solution()

print(a.letterCombinations("23"))

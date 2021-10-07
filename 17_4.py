class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        d2sMap={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        return self.recursive([],digits,d2sMap)

    def recursive(self,res,digit,dic):
        if digit=="":
            return res

        new_res=[]
        for v in dic[digit[0]]:
            if len(res)==0:
                new_res.append(v)

            for i in range(len(res)):
                new_res.append(res[i]+v)
        return self.recursive(new_res,digit[1:],dic)
digits = "23"

a=Solution()
print(a.letterCombinations(digits))


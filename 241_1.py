class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """

        return self.divideConquer(expression)




    def divideConquer(self,expression):
        if expression.isdigit():
            return int(expression)

        res=[]
        for i in range(len(expression)):
            if expression[i] in ["+","-","*","/"]:
                left=self.divideConquer(expression[:i])
                right=self.divideConquer(expression[i+1:])
                for ii in left:
                    for jj in right:
                        if expression[ii]=="+":
                            res.append(int(ii)+int(jj))
                        elif expression[ii]=="-":
                            res.append(int(ii)-int(jj))
                        elif expression[ii]=="*":
                            res.append(int(ii)*int(jj))
                        else:
                            if jj!=0:
                                res.append(int(ii)/int(jj))
        return res





    ##最初的想法是按照第一个数字是否直接和右边的数结合进行dfs，但是结果中有漏掉的
    def dfs(self,expression,res):
        # print(expression,res)
        if len(expression)==3:
            res.append(int(self.compute(expression)))
        else:
            tmp=self.compute(expression[:3])
            # print(tmp)
            if tmp!=float("inf"):
                newexp=[tmp]
                newexp.extend(expression[3:])
                self.dfs(newexp,res)
            leftres=[]
            self.dfs(expression[2:],leftres)
            for v in leftres:
                newexp=expression[:2]
                newexp.append(v)
                res.append(self.compute(newexp))



    def compute(self,exp):
        print(exp)
        if exp[1]=="+":
            return int(exp[0])+int(exp[2])
        elif exp[1] == "-":
            return int(exp[0]) - int(exp[2])
        elif exp[1] == "*":
            return int(exp[0]) *int(exp[2])
        elif exp[1] == "/":
            if exp[2]=="0":
                return float("inf")
            return int(exp[0])/int(exp[2])


    def splitStr(self,exp):
        i=0
        tmpstr=""
        exp+="+"
        res=[]
        while i<len(exp):
            if exp[i] in ["+","-","*","/"]:
                res.append(tmpstr)
                res.append(exp[i])
                tmpstr=""
            else:
                tmpstr+=exp[i]
            i+=1
        res=res[:-1]
        return res

test="2*3-4*5"
a=Solution()
print(a.diffWaysToCompute(test))

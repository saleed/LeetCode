class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """

        return self.recursive(expression)




    def recursive(self,expression):
        res=[]

        findFlag=0
        for i in range(len(expression)):
            if expression[i] in ["+","-","*","/"]:
                findFlag=1
                left=self.recursive(expression[:i])
                right=self.recursive(expression[i+1:])
                for v1 in left:
                    for v2 in right:
                        if expression[i] =="+":
                            res.append(v1+v2)
                        elif expression[i]=="-":
                            res.append(v1 + v2)
                        elif expression[i]=="*":
                            res.append(v1 + v2)
                        elif expression[i]=="/":
                            res.append(v1 + v2)
        if findFlag==0:
            return int(expression)
        return res





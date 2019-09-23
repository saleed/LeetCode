class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        st=[]
        for i in tokens:
            if self.isOperator(i):
                data2=st.pop()
                data1=st.pop()
                # print data2,data1
                newdata=self.opWithData(i,data1,data2)
                # print newdata
                st.append(newdata)
            else:
                st.append(i)
            print st
        # print st
        if len(st)==1:
            return int(st.pop())
        else:
            return -1



    def isOperator(self,tokens):
        return tokens=='+' or  tokens=='-' or  tokens=='*' or  tokens=='/'
    def opWithData(self,op,d1,d2):
        d1=int(d1)
        d2=int(d2)
        res=0
        # print op
        if op=='+':
            res= d1+d2
        if op == '-':
            res = d1-d2
        if op == '*':
            res = d1*d2
        if op == '/':
            if d1<0 or d2<0:
                res=abs(d1)/abs(d2)*(-1)
            else:
                res = d1/d2
        return str(res)


test=["2","1","+","3","*"]
a=Solution()
print a.evalRPN(test)
test=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print a.evalRPN(test)
print 6/(-132) ##=1
print 6/132 #0
print -5/2
test=["4","-2","/","2","-3","-","-"]
print a.evalRPN(test)

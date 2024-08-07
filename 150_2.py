class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        st=[]
        for i in tokens:
            if self.isOp(i):
                d2=int(st.pop())
                d1=int(st.pop())
                st.append(self.compute(d1,d2,i))
            else:
                st.append(int(i))
        return st[0]





    def isOp(self,ch):
        return ch=='+' or ch=='-' or ch=='*'or ch=='/'
    def compute(self,d1,d2,op):
        if op=='+':
            return d1+d2
        if op=='-':
            return d1-d2
        if op=='*':
            return d1*d2
        if op=='/':
            if d1<0 or d2<0:
                return abs(d1)/abs(d2)*(-1)
            else:
                return d1/d2


a=Solution()

test=["2", "1", "+", "3", "*"]

print(a.evalRPN(test))

print(int("-2323"))

print("-11".isdigit())  ###只能判断正数

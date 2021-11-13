class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        st=[]
        opset=set(["+","-","*","/"])
        for v in tokens:
            if v in opset:
                v2=st.pop()
                v1=st.pop()
                st.append(str(self.calu(int(v1),int(v2),v)))
            else:
                st.append(v)
        return st.pop()


    def calu(self,v1,v2,op):
        flag=1
        if v1*v2<0:
            flag=-1
        if op=="+":
            return v1+v2
        if op=="-":
            return v1-v2
        if op=="*":
            return v1*v2
        if op=="/":
            return abs(v1)/abs(v2)*flag



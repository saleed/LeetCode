class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        if len(expression)<2:
            return expression

        v=expression[0]
        maohaoid=-1
        st=[]
        for i in range(len(expression)):
            if expression[i]==":" and len(st)==0:
                maohaoid=i
            elif expression[i]=="?":
                st.append(1)
            elif expression[i]==":":
                st.pop()
        if v=="T":
            return self.parseTernary(expression[2:maohaoid])
        else:
            return self.parseTernary(expression[maohaoid+1:])


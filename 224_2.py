import copy

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=self.removeSpace(s)
        return self.caculateStr([0,0],['+','+'],s)



    def caculateStr(self,preVal,preOp,s):
        print(preVal,preOp,s)
        p=0
        pre1=preVal[0]
        pre2=preVal[1]
        op=preOp[0]
        curop=preOp[1]
        if curop=='#':
            if op=='+':
                return pre1+pre2
            elif op=='-':
                return pre1-pre2
            else:
                return pre1*pre2
        elif curop=='*':
            if s[0]=='(':
                pos=self.getBracketPos(s)
                pre2*=self.caculateStr([0,0],['+','+'], s[1:pos])
                p=pos+1
            else:
                p=self.getNextStr(s)
                pre2=pre2*int(s[:p])
            print(pre1, pre2)
        elif curop=='+' or curop=='-' :
            if op=='+':
                pre1+=pre2
            elif op=='-':
                pre1-=pre2
            else:
                pre1*=pre2
            if s[0] == '(':
                pos = self.getBracketPos(s)
                pre2 = self.caculateStr([0,0],['+','+'], s[1:pos])
                p = pos + 1
            else:
                p = self.getNextStr(s)
                pre2 = pre2 * int(s[:p])
            print(pre1, pre2)

        # print(pre1,pre2)
        if p == len(s):
            return self.caculateStr([pre1,pre2], [curop, '#'], "")
        else:
            return self.caculateStr([pre1,pre2], [curop,s[p]], s[p + 1:])

    def getNextStr(self,s):
        if len(s)==0:
            return '0'
        p = 0
        while p<len(s):
            if s[p]<='9' and s[p]>='0':
                p+=1
            else:
                break

        return p


    def getBracketPos(self,s):
        st=[]
        q = 0
        while q < len(s):
            if s[q] == ')':
                st.pop()
            if s[q] == '(':
                st.append('(')
            if len(st) == 0:
                break
            q+=1
        return q




    def removeSpace(self,s):
        res=""
        for i in s:
            if i!=" ":
                res+=i
        return res


a=Solution()
# s="1 + 1"
# print(a.calculate(s))
# s=" 2-1 + 2 "
# print(a.calculate(s))
s="(1+(4+5+2)-3)+(6+8)"
print(a.calculate(s))
print(a.getBracketPos(s))


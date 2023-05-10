class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i=0
        ans=""
        add="0"
        while len(num1)-i-1>=0:
            mul=self.onebitMulti(num2,num1[i])
            add=self.stradd(add,mul+'0'*i)
        return add

    def onebitMulti(self,num,ch):
        res=""
        c=0
        i=0
        while len(num)-1-i>=0:
            c=(int(num[i])*int(ch)+c)/10
            res=str(int(num[i])*int(ch)+c)%10+res
            i+=1
        return res





    def stradd(self,num1,num2):
        if len(num1)<len(num2):
            num1,num2,=num2,num1
        i=0
        res=""
        c=0
        while i<max(len(num2),len(num1)):
            d1=int(num1[len(num1)-1-i]) if len(num1)-1-i>=0 else 0
            d2=int(num2[len(num2)-1-i]) if len(num2)-1-i>=0 else 0
            c=(d1+d2)/10
            res=str((d1+d2+c)%10)+res
        if c:
            res=str(c)+res
        return res


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1=="0" or num2=="0":
            return "0"
        res=""
        for s in num2:
            res+='0'
            tmp=self.Onebitmutiply(num1,s)
            res=self.stringadd(res,tmp)
        return res



    def stringadd(self,str1,str2):
        if len(str1)==0 or len(str2)==0:
            return ""

        if len(str1)<len(str2):
            str1,str2=str2,str1

        str2='0'*(len(str1)-len(str2))+str2
        # print(str2)

        res=""
        c=0
        for i in range(len(str1))[::-1]:
            res=str((int(str1[i])+int(str2[i])+c)%10)+res
            c=(int(str1[i])+int(str2[i])+c)//10

        if c>0:
            res=str(c)+res

        return res





    def Onebitmutiply(self,ch,strs):

        res=""
        c=0
        for s in strs[::-1]:
            res=str((int(s)*int(ch)+c)%10)+res
            c=(int(s)*int(ch)+c)//10
        if c:
            res=str(c)+res

        return res


a=Solution()
print(a.Onebitmutiply("1111","2"))
print(a.stringadd("111","1"))

print(5*'0')
print(a.multiply("16","16"))

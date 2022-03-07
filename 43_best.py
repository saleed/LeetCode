class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res="0"
        for i in range(len(num1))[::-1]:
            tmp=self.bitMultiply(num2,num1[i])
            print(res,tmp)
            res=self.bitAdd(tmp+'0'*(len(num1)-1-i),res)

        return res


    def bitMultiply(self,mstr,bit):
        res=""
        c=0
        for i in range(len(mstr))[::-1]:
           res=str((int(mstr[i])*int(bit)+c)%10)+res
           c=(int(mstr[i])*int(bit)+c)/10

        if c>0:
            res=str(c)+res
        return res


    def bitAdd(self,str1,str2):
        res=""
        c=0

        if len(str1)>len(str2):
            str2="0"*(len(str1)-len(str2))+str2

        else:
            str1="0"*(len(str2)-len(str1))+str1

        for i in range(len(str1))[::-1]:
            res=str((int(str1[i])+int(str2[i])+c)%10)+res
            c=(int(str1[i])+int(str2[i])+c)/10

        if c>0:
            res=str(c)+res
        # print(str1,str2,res)
        return res
a=Solution()
print(a.multiply("123","456"))
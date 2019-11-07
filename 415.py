class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1)>len(num2):
            num1,num2=num2,num1


        num1="0"*(len(num2)-len(num1))+num1
        c=0
        res=""
        for i in range(len(num1))[::-1]:
            res=str((int(num1[i])+int(num2[i])+c)%10)+res
            c=int((int(num1[i])+int(num2[i])+c)/10)

        if c:
            res="1"+res
        return res



a=Solution()
print(a.addStrings("999","1"))
print(a.addStrings("99","9"))


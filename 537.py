class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        add1=num1.find("+")
        add2=num2.find("+")
        real1=num1[:add1]
        comp1=num1[add1+1:-1]
        real2=num2[:add2]
        comp2=num2[add2+1:-1]

        real3=int(real1)*int(real2)-int(comp1)*int(comp2)
        comp3=int(real1)*int(comp2)+int(real2)*int(comp1)

        return str(real3)+"+"+str(comp3)+"i"


ss=Solution()
print(ss.complexNumberMultiply("1+-1i","0+0i"))
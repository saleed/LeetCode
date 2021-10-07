class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res="0"
        for i in list(reversed(range(len(num2)))):
            mul=self.mulbit(num1,num2[i])
            res=self.add(res,mul+(len(num2)-i-1)*'0')
            # print(mul,mul+(len(num2)-i-1)*'0',res)

        i=0
        while  i < len(res):
            if res[i]=='0':
                i+=1
            else:
                break
        return "0" if i==len(res) else res[i:]





    def mulbit(self,nums1,b):
        c=0
        res=""
        for i in list(reversed(range(len(nums1)))):
            mul=(int(nums1[i])*int(b))+c
            c=mul/10
            left=mul%10
            res=str(left)+res
        if c>0:
            res=str(c)+res
        return res


    def add(self,nums1,nums2):

        c=0
        res=""
        for i in range(max(len(nums1),len(nums2))):
            v1=nums1[len(nums1)-1-i] if len(nums1)-1-i>=0 else 0
            v2=nums2[len(nums2)-1-i] if len(nums2)-1-i>=0 else 0
            vsum=(c+int(v1)+int(v2))
            res=str(vsum%10)+res
            c=vsum/10
        if c>0:
            res=str(c)+res

        return res



if __name__=="__main__":
    a=Solution()
    num1 = "123"
    num2 = "456"
    print(a.multiply(num1,num2))

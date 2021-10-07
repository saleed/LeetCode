class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        zeroNum=0
        if num1=="0" or num2=="0":
            return "0"
        res="0"
        for p in num1[::-1]:
            multi=self.multiplyOneBit(num2,p)
            res=self.sumTwoString(res,multi+zeroNum*"0")
            print(multi)
            zeroNum+=1


        return res


    def multiplyOneBit(self,nums,bitchar):
        c=0
        res=""
        for val in nums[::-1]:
            muti=int(val)*int(bitchar)+c
            c=muti/10
            res=str(muti%10)+res
        if c>0:
            res=str(c)+res
        return res

    def sumTwoString(self,nums1,nums2):
        p=len(nums1)-1
        q=len(nums2)-1
        c=0
        res=""
        while p>=0 or q>=0:
            if p<0:
                pval=0
            else:
                pval=int(nums1[p])
                p-=1
            if q<0:
                qval=0
            else:
                qval=int(nums2[q])
                q-=1
            sumval=pval+qval+c
            c=sumval/10
            res=str(sumval%10)+res
        if c>0:
            res="1"+res
        return res


if __name__=="__main__":
    a=Solution()
    num1 = "123"
    num2 = "456"
    print(a.multiply(num1,num2))










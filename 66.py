class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        c=1
        for i in range(len(digits))[::-1]:
           tmp=digits[i]
           digits[i]=int(tmp+c)%10
           c=int((tmp+c)/10)

        res=digits[:]
        if c:
            res=[1]+res

        return res

a=Solution()
print(a.plusOne([1,2,3]))
print(a.plusOne([9,9,9]))

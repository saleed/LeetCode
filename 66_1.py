class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits)==0:
            return None
        c=(digits[-1]+1)/10
        digits[-1]=(digits[-1]+1)%10
        p=len(digits)-2
        while c and  p>=0:
            tmp=digits[p]
            digits[p]=(tmp+c)%10
            c=(tmp+c)/10
            p-=1
        if c>0:
            res=[1]
            res.extend(digits)
            digits=res
        return digits
test=[9,9]
a=Solution()
print(a.plusOne(test))




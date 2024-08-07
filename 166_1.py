class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        flag=1
        if numerator*denominator<0:
            flag=-1
        if numerator==0:
            return "0"

        div=abs(numerator)/abs(denominator)
        upzero=str(div)
        left=abs(numerator)%abs(denominator)
        if left==0:
            return upzero
        downzero=""
        divmap={}
        while left not in divmap:
            div=(left*10)/abs(denominator)

            downzero+=str(div)
            divmap[left]=len(downzero)-1
            left=(left*10)%abs(denominator)
            if left==0:
                break
        if left>0:
            downzero=downzero[:divmap[left]]+"("+downzero[divmap[left]:]+")"
        res=str(str(upzero)+"."+downzero)
        if flag<0:
            res="-"+res
        return res


numerator =-1
denominator =-2147483648
a=Solution()
print(a.fractionToDecimal(numerator,denominator))

# print(1/2147483648)
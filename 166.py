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

        numerator=abs(numerator)
        denominator=abs(denominator)
        mtZero=abs(numerator)/abs(denominator)
        left=abs(numerator)%abs(denominator)


        if left==0:
            return str(flag*mtZero)
        ltZero=""

        leftdict={}
        cnt=0
        while left!=0:
            div=(left*10)/denominator
            left=(left*10)%denominator
            ltZero += str(div)
            if left in leftdict.keys():
                id=leftdict[left]
                ltZero=ltZero[:id+1]+"("+str(ltZero[id+1:])+")"
                break
            else:
                leftdict[left]=cnt
            cnt+=1



        if flag==-1:
            return "-"+str(mtZero)+"."+ltZero
        else:
            return str(mtZero)+"."+ltZero

a=Solution()
print(a.fractionToDecimal(7,-12))

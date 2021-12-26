class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """

        ##两种思路，一种是按照低位到高位
        ##第二种思路是n拆分成整数
        res=0
        div=10
        while div/10<n:
            res+=n/div*(div/10)
            if n%div/(div/10)==1:
                res+=(n%div)%10+1
            elif n%div/(div/10)>1:
                res+=(div/10)
            div*=10
        return res



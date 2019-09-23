class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        res=0
        charr=['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
        vararr=[1,4,5,9, 10,40,50,90,100,400,500,900,1000]
        # ptr=len(charr)
        while len(s)>0:
            # print(s)
            for i in list(reversed(range(len(charr)))):
                if s[:len(charr[i])]==charr[i]:
                    res+=vararr[i]
                    s=s[len(charr[i]):]
                    break
        return res
a=Solution()
print(a.romanToInt('MCMXCIV'))
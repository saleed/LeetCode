class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        p=0

        cdict = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        vdict = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        res=0
        while p<len(s):
            for i in range(len(cdict))[::-1]:
                if p+len(cdict[i])<len(s) and cdict[i]==s[p:p+len(cdict[i])]:
                    res+=vdict[i]
                    p+=len(cdict[i])
                    break
        return res


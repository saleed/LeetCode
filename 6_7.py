class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        T=2*numRows-2
        res=""

        for i in range(numRows):
            if i==0 or i==numRows-1:
                n=0
                while i+n*T<len(s):
                    res+=s[i+n*T]
                    n+=1
                print(res)
            else:
                n=0
                while True:
                    if i+n*T<len(s):
                        res += s[i + n * T]
                    else:
                        break
                    if (n+1)*T-i<len(s):
                        res += s[(n+1)*T-i]
                    else:
                        break
                    n+=1
        return res







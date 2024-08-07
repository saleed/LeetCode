class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s

        T=2*numRows-2
        res=""
        for i in range(numRows):
            if i==0 or i==numRows-1:
                n=0
                while n*T+i<len(s):
                    res+=s[n*T+i]
                    n+=1
                    # print(1)
            else:
                n=0
                while True:
                    if n*T+i<len(s):
                        res += s[n * T + i]
                    else:
                        break
                    if(n+1)*T-i < len(s):
                        res +=s[(n+1)*T-i]
                    else:
                        break
                    n+=1
                    # print(2)
        return res

s = "A"
numRows = 1
a=Solution()
print(a.convert(s,numRows))
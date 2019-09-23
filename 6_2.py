class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res=""
        if numRows==1:
            return s
        T=int(len(s)/(2*numRows-2))
        r=0
        while r<numRows:
            for t in range(T+1):
                if r==0 or r==numRows-1:
                    if t*(2*numRows-2)+r<len(s):
                        res+=s[t*(2*numRows-2)+r]
                else:
                    if t*(2*numRows-2)+r<len(s):
                        res+=s[t*(2*numRows-2)+r]
                    if (t+1)*(2*numRows-2)-r<len(s):
                        res+=s[(t+1)*(2*numRows-2)-r]
            r+=1
        return res


test="LEETCODEISHIRING"
b=Solution()


print(b.convert(test,3))

test="PAYPALISHIRING"

print(b.convert(test,3))
#
# "PAHNAALAISGRYIR"
# "PAHNAPLSIIGYIR"


print(b.convert('A',1))
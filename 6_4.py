    class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        step=2*numRows-2
        res=""

        for i in range(numRows):
            if i==0 or i==numRows-1:
                start=i
                while start<len(s):
                    res+=s[start]
                    start+=step
            else:
                start1=i
                start2=step-i
                while start1<len(s) or start2<len(s):
                    if start1<len(s):
                        res+=s[start1]
                        start1+=step
                    if start2<len(s):
                        res+=s[start2]
                        start2+=step
        return res


test="LEETCODEISHIRING"
b=Solution()


print(b.convert(test,3))

test="PAYPALISHIRING"

print(b.convert(test,3))

# "PAHNAALAISGRYIR"
# "PAHNAPLSIIGYIR"


print(b.convert('A',1))


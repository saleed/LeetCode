class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        T=numRows+numRows-2
        if T==0:
            return s
        ret=""
        for i in range(numRows):
            if i==0 or i==numRows-1:
                t=0
                while i+t*T<len(s):
                    ret+=s[i+t*T]
                    t+=1
            else:
                t=0
                while i+t*T<len(s) or T-i+t*T<len(s):
                    if i+t*T<len(s):
                        ret+=s[i+t*T]
                    if T-i+t*T<len(s):
                        ret+=s[T-i+t*T]
                    t+=1
        return ret


if __name__=="__main__":
    a=Solution()
    s = "PAYPALISHIRING"
        "PAHNAPLSIIGYIR"
        "PAHNAPLSIIGYIR"
    numRows = 3
    print(a.convert(s,numRows))

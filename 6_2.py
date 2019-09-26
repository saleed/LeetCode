#很经典的一道题：
# 其实就是考察如何把一个数映射成既定规则的行列二维表示：
    1.首先可以确定Z字形，形状是周期性的，一个周期包含的字符串数位T=2*row-2,占据的行数为n-1
    2.根据上述结论，就可以对每行进行讨论：
        首先考虑首行和末行，他们的字符数为n/T，起始点为行数
        在考虑中间的行，他们的字符数为2*n/T 分成两部分，第一部分七十点为行数 周期为T  第二部门起始点为2*row-2-行数，周期同样为T

    这样遍可以依次打出所有的字符





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
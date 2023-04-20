class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res=""
        T=2*numRows-2
        if numRows==0:  ###注意这里
            return s

        for i in range(numRows):
            j=0
            while j<(len(s)/T+1):
                if i==0 or i==numRows-1:
                    if j*T+i<len(s):
                        res+=s[j*T+i]
                else:
                    if j*T+i<len(s):
                        res+=s[j*T+i]
                        # print(j*T+i)
                    if 0<=j*T+T-i<len(s):
                        res+=s[j*T+T-i]  ##注意这里，不能写成j*(T+1)-i
                # print(j * T + i, j*T+T-i, res)
                j+=1

        return res


    def convert2(self, s, numRows):
        if numRows==1:
            return s
        res=["" for _ in range(numRows)]
        i=0
        flag=-1
        for c in s:
            res[i]+=c
            if i==0 or i==numRows-1:  ###还是要注意numRows=1的情况
                flag*=-1
            i+=flag
        return "".join(res)




if __name__=="__main__":
    a=Solution()
    s = "PAYPALISHIRING"
    numRows = 3
    print(a.convert(s,numRows))

    "PAHNAPLSIIGYIR"
    "PAHNAGLAIIGYIR"





            



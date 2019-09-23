class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        return self.GetMappingCordinate(s,row)

    def simulate(self,s,row):
        mat=[["" for _ in range(int(len(s)/2)+1)] for _ in range(row)]
        print(len(mat),len(mat[0]))
        count=0
        r=-1
        c=0
        while count<len(s):
            while r+1<row and count<len(s):
                r+=1
                mat[r][c]=s[count]
                count+=1
            while r-1>=0 and count<len(s):
                print(r,c)
                r-=1
                c+=1
                mat[r][c]=s[count]
                count+=1
        res=""
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]!="":
                    res+=mat[i][j]
        return res


    def GetMappingCordinate(self,s,row):

        res=""
        T=2*row-2
        for i in range(row):
            if i==0 or i==row-1:
                j=0
                while j*T+i<len(s):
                    res+=s[j*T+i]
                    j+=1
            else:
                j=0
                while j*T+i<len(s) or j*T-i<len(s):
                    if j*T+i<len(s):
                        res+=s[j*T+i]
                    if j * T - i < len(s):
                        res+=s[j*T-i]
                    j+=1
        return res






a=Solution()

s="LEETCODEISHIRING"
row=3
# print(a.simulate(s,row))
print(a.GetMappingCordinate(s,row))
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.strip(" ")
        flag=1
        res=0
        if len(s)>0:
            if s[0]=="-":
                flag=-1
                s=s[1:]
            elif s[0]=="+":
                flag=1
                s=s[1:]
            for i in s:
                if i>='0' and i<='9':
                    res=res*10+int(i)
                else:
                    break

        if res*flag<=-pow(2,31):
            return -pow(2,31)
        if res*flag>=pow(2,31)-1:
            return pow(2,31)-1
        return res*flag

a=Solution()
print(a.myAtoi("-91283472332"))



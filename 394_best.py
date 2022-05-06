class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=""
        i=0
        while i<len(s):
            if s[i].isalpha():
                res+=s[i]
                i+=1
            elif s[i].isdigit():
                digit=""
                while s[i].isdigit():
                    digit+=s[i]
                    i+=1
                st=1
                i+=1
                p=i
                while st>0:
                    if s[i]=='[':
                        st+=1
                    elif s[i]==']':
                        st-=1
                    i+=1

                tmpstr=s[p:i-1]
                res+=int(digit)*self.decodeString(tmpstr)

        return res




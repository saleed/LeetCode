class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        pre=""
        return self.match(s,p,pre)

    def match(self,s,p,pre):
        if s=="" and p=="":
            return True
        if len(s)>0 and len(p)>0:
            if p[0]!="." and p[0]!="*" and p[0]==s[0]:
                return self.match(s[1:],p[1:],p[0])
            if p[0]==".":
                return self.match(s[1:],p[1:],".")
            if p[0]=="*":
                if pre==".":
                    i=0
                    while i<len(s):
                        if self.match(s[i:],p[1:],"."):
                            return True
                        i+=1
                elif pre=="*":
                    print("igonre")

                else:
                    i=0
                    while i<len(s):
                        if self.match(s[i:],p[1:],s[0]):
                            return True
                        i+=1
        return False



if __name__=="__main__":
    a=Solution()
    s = "aab"
    p = "c*a*b"





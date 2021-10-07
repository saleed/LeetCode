##逻辑正确，超时

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.matchRecursive(s,p)



    def matchRecursive(self,s,p):
        print(s,p)
        if s=="" and p=="":
            return True
        if p!="":
            if len(p)>1 and p[1]=="*":
                if p[0]==".":
                    for i in range(len(s)+1):
                        # print(i)
                        if self.matchRecursive(s[i:],p[2:]):
                            return True
                    return False
                else:
                    if self.matchRecursive(s,p[2:]):
                        return True
                    for i in range(len(s)):
                        # print(i)
                        if s[i]==p[0]:
                            if self.matchRecursive(s[i+1:],p[2:]):
                                return True
                        else:
                            return False
                    return False
            else:
                if len(s)>0:
                    if p[0]==".":
                        return self.matchRecursive(s[1:],p[1:])
                    else:
                        if s[0]==p[0]:
                            return self.matchRecursive(s[1:],p[1:])
                        return False
                return False
        return False

s="a"
p=".*..a*"
s="aaaaaaaaaaaaab"
p="a*a*a*a*a*a*a*a*a*a*c"
a=Solution()
print a.isMatch(s,p)
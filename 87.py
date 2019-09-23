class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1)==1:
            return s1==s2
        elif len(s1)==2:
            return s1[0]==s2[1] and s1[1]==s2[0]
        else:
            if set(s1)!=set(s2):
                return False
            for i in range(len(s1)-1):
                if self.isScramble(s1[:i+1],s2[:i+1]) and self.isScramble(s1[i+1:],s2[i+1:]):
                    return True
            return False









s1="abc"
print(set(s1))
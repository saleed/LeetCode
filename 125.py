class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        p=0
        q=len(s)-1
        while p<q:
            if self.isAlphaorDigit(s[p]) and self.isAlphaorDigit(s[q]):
                if s[p].lower()!=s[q].lower():
                    return False
                else:
                    p+=1
                    q-=1
            elif not self.isAlphaorDigit(s[p]):
                p+=1
            elif not self.isAlphaorDigit(s[q]):
                q-=1
        return True




    def isAlphaorDigit(self,s):
        return (s>='a' and s<='z') or  (s>='A' and s<='Z') or  (s>='0' and s<='9')

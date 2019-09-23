class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s=="":
            return ""
        for i in list(reversed(range(len(s)))):
            if s[:i+1]==s[:i+1][::-1]:
                return s[i+1:][::-1]+s






    def JundgePalindrome(self,s,id):
        p=0
        q=id
        while p<q:
            if s[p]!=s[q]:
                return False
            p+=1
            q-=1
        return True

a=Solution()
t="aacecaaa"
# print(list(reversed()))
print(a.shortestPalindrome(t))

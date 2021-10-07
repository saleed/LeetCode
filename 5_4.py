class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """


        return self.solve1(s)





    def solve1(self,s):

        maxLen=0
        maxStr=""

        for i in range(len(s)):
            for l in range(len(s)):
                if i+l<len(s) and i-l>=0 and s[i+l]==s[i-l]:
                    if 1+2*l>maxLen:
                        maxLen=1+2*l
                        maxStr=s[i-l:i+l+1]
                else:
                    break
        for i in range(len(s)):
            for l in range(len(s)):
                if i-l>0 and i+1+l<len(s) and s[i+l]==s[i+1+l]:
                    if 2+l*2>maxLen:
                        maxLen=2+2*l
                        maxStr=s[i-l:i+l+2]
                else:
                    break
        return maxStr

s="a"
a=Solution()
print(a.longestPalindrome(s))
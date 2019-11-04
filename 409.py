class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        sett=set()
        pairNum=0
        for i in s:
            if i in sett:
                sett.remove(i)
                pairNum+=1
            else:
                sett.add(i)
        return 2*pairNum if len(sett)==0 else 2*pairNum+1

a=Solution()
print(a.longestPalindrome("abccccdd"))
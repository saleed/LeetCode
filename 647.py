class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """



        res=0
        for i in range(len(s)):
            l=i
            r=i
            cnt=0
            while l>=0 and r<len(s) and s[l]==s[r]:
                cnt+=1
                l-=1
                r+=1

            l=i
            r=i+1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1

            res+=cnt
        return cnt
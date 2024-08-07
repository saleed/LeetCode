class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="":
            return 0
        lmax=0
        res=0
        sdict={}
        for i in range(len(s)):
            if s[i] not in sdict:
                sdict[s[i]]=i
            else:
                lmax=max(lmax,sdict[s[i]])
                sdict[s[i]]=i
            res=max(res,i-lmax)
        return res


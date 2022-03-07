class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        # """


        max_len=0
        lptr=-1 ###-1
        vdict={}
        for rptr in range(len(s)):
            if s[rptr]  not in vdict:
                vdict[s[rptr]]=rptr
            else:
                lptr=max(lptr,vdict[s[rptr]])
                vdict[s[rptr]]=rptr
            max_len=max(max_len,rptr-lptr)
        return max_len
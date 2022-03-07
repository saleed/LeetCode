class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        # """
        pos=dict()
        maxl=0
        l=0
        for i in range(len(s)):
            if s[i] in pos:
                l=i-pos[s[i]]
            else:
                l+=1
            pos[s[i]] = i
            maxl = max(maxl, l)
        return maxl

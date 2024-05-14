class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        pos_dict=dict()
        left=-1
        maxl=0
        for i in range(len(s)):
            if s[i] not in pos_dict:
                pos_dict[s[i]]=i
                maxl = max(maxl, i-left)
            else:
                left=max(left,pos_dict[s[i]])
                maxl = max(maxl, i-left)
                pos_dict[s[i]]=i
        return maxl





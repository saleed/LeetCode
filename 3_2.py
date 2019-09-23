class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="":
            return 0
        dict={}
        start=0
        maxlen=1
        for end in range(len(s)):
            if s[end] not in dict.keys():
                dict[s[end]]=1
                maxlen=max(maxlen,end-start+1)
            else:
                while s[start]!=s[end]:
                    if dict[s[start]]==1:
                        del dict[s[start]]
                    else:
                        dict[s[start]]-=1
                    start+=1
                start+=1
        return maxlen





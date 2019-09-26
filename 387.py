class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return -1
        dict={}
        for i in range(len(s)):
            if s[i] in dict.keys():
                dict[s[i]]=len(s)
            else:
                dict[s[i]]=i
        minv=float("inf")
        for i in dict.keys():
            if dict[i]!=len(s):
                minv=min(minv,dict[i])
        return minv if minv!=float("inf") else -1


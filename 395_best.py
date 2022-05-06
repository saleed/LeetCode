class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        numdict={}
        for i in range(len(s)):
            if s[i] in numdict:
                numdict[s[i]]+=1
            else:
                numdict[s[i]]=1
        selk=""
        for key in numdict:
            if numdict[key]<k:
                selk=key


        if selk=="":
            return len(s)
        maxlen=0
        pre=0
        s+=selk
        for i in range(len(s)):
            if s[i]==selk:
                maxlen=max(maxlen,self.longestSubstring(s[pre:i],k),)
                pre=i+1
        return maxlen




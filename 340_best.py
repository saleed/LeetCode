class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k==0:
            return 0
        maxlen=0
        posdict={}
        left=-1
        for i in range(len(s)):
            if len(posdict)<k:
                posdict[s[i]]=i
            else:
                if s[i] in posdict:
                    posdict[s[i]]=i
                else:
                    mink=-1
                    minv=float("inf")
                    for key in posdict:
                        if posdict[key]<minv:
                            mink=key
                            minv=posdict[key]
                    left =posdict[mink]
                    del posdict[mink]
                    posdict[s[i]]=i
            maxlen=max(maxlen,i-left)
        return maxlen



t="aba"
k=1
s=Solution()
print(s.lengthOfLongestSubstringKDistinct(t,k))

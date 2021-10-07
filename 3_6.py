class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="":
            return 0
        dp=[0]*len(s)
        dict={}
        for i in range(len(s)):
            print(dict)
            if s[i] in dict.keys():
                dp[i]=min(dp[i-1]+1,i-dict[s[i]])
                dict[s[i]]=i
            else:
                dp[i]=dp[i-1]+1
                dict[s[i]]=i

        print(dp)
        return max(dp)

a=Solution()
s= "pwwkew"
print(a.lengthOfLongestSubstring(s))
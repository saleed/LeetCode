class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0

        dict={}
        start=0
        maxlen=0
        for i in range(len(s)):
            ch=s[i]
            if ch not in dict.keys():
                dict[ch]=i
            else:
                newstart=dict[ch]+1
                for j in range(start,newstart):
                    del dict[s[j]]
                start=newstart
                dict[ch]=i

            maxlen=max(maxlen,i-start+1)

        return maxlen





a=Solution()


print(a.lengthOfLongestSubstring("abc"))
print(a.lengthOfLongestSubstring("abcdae"))
print(a.lengthOfLongestSubstring("aaaaa"))
print(a.lengthOfLongestSubstring("ababab"))
print(a.lengthOfLongestSubstring("aab"))
print(a.lengthOfLongestSubstring(" "))




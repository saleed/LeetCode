class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        ss=set()
        start=0
        maxlen=1
        ss.add(s[0])
        for j in range(1,len(s)):
            if s[j] not in ss:
                ss.add(s[j])
                maxlen=max(maxlen,j-start+1)
            else:
                while s[start]!=s[j]:
                    ss.remove(s[start])
                    start+=1
                start+=1
        return maxlen





a=Solution()


print(a.lengthOfLongestSubstring("abc"))
print(a.lengthOfLongestSubstring("abcdae"))
print(a.lengthOfLongestSubstring("aaaaa"))
print(a.lengthOfLongestSubstring("ababab"))
print(a.lengthOfLongestSubstring("aab"))
print(a.lengthOfLongestSubstring(" "))




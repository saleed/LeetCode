class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s.strip()
        return len(s.split(" ")[-1])

a=Solution()
test="Hello World"
print(a.lengthOfLastWord(test))
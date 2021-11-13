class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        i = 0
        start = i
        while i < len(s):
            while i < len(s) and s[i].isalpha():
                i += 1
            j = i - 1
            while start < j:
                s[start], s[j] = s[j], s[start]
                start += 1
                j -= 1
            while i < len(s) and not s[i].isalpha() :
                i += 1
            start = i





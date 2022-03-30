class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        q = 0
        while q < len(s):
            while s[q] == " ":
                q += 1
            p = q
            while s[q] != " " and q < len(s):
                q += 1
            self.reverse(p, q, s)

    def reverse(self, p, q, s):
        while p < q<len(s):
            s[p], s[q] = s[q], s[p]
            p += 1
            q -= 1

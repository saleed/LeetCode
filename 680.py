class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        p = 0
        q = len(s) - 1

        while p < q:
            if s[p] != s[q]:
                if s[p + 1] == s[q] and self.check(s, p + 1, q):
                    return True
                elif s[p] == s[q - 1] and self.check(s, p, q - 1):
                    return True
                else:
                    return False
            else:
                p += 1
                q -= 1
        return True

    def check(self, s, p, q):
        while p < q:
            if s[p] != s[q]:
                return False
            p += 1
            q -= 1
        return True



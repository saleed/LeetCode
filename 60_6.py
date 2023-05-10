class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        sel = [i + 1 for i in range(n)]
        i = len(sel) - 1
        k = k - 1
        ans = ""
        while i >= 0:
            fac = self.fac(i)
            idx = k / fac
            k = k % fac
            ans += str(sel[idx])
            sel.remove(sel[idx])
            i -= 1
        return ans

    def fac(self, i):
        if i == 0:
            return 1
        else:
            return i * self.fac(i - 1)

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        l = max(len(a), len(b))
        i = 1
        res = ""
        c = 0
        while i <= l:
            va = 0 if len(a) - i < 0 else int(a[len(a)-i])
            vb = 0 if len(b) - i < 0 else int(b[len(b)-i])
            res = str((vb+va+c)%2)+res
            c = (va + vb) / 2
            i+=1
        if c > 0:
            res = "1" + res
        return res


a = "1010"
b = "1011"
c=Solution()
print(c.addBinary(a,b))
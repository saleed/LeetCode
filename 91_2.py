class Solution:
    def numDecodings(self, s: str) -> :
        n = len(s)
        f = [1] + [0] * n
        for i in range(1, n + 1):
            if s[i - 1] != '0':
                f[i] += f[i - 1]
            if i > 1 and s[i - 2] != '0' and int(s[i-2:i]) <= 26:
                f[i] += f[i - 2]

        print(f)
        return f[n]

test="2611055971756562"
a=Solution()
print(a.numDecodings(test))

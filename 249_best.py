class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        hashdict = {}
        for v in strings:
            tk = self.convert(v)
            if tk in hashdict:
                hashdict[tk].append(v)
            else:
                hashdict[tk] = [v]

        return hashdict.values()

    def convert(self, s):
        res = ""
        diff = ord(s[0]) - ord('a')
        for v in s:
            res += chr((ord(v) - diff - ord('a') + 26) % 26)
        print(res)
        return res

test="dfaggagag"
a=Solution()
print(a.convert(test))

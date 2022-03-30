class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        maxv=-float("inf")

        bitdict=self.bitConvert(words)

        for k1 in bitdict:
            for k2 in bitdict:
                if k1&k2==0:
                    maxv=max(maxv,bitdict[k1]*bitdict[k2])



        return maxv


    def bitConvert(self,words):
        bitdict={}
        for v in words:
            res=0
            for ch in v:
                res=res|1<<(ord(ch)-ord('a'))
            if (res not in bitdict) or (res in bitdict and bitdict[res]<len(v)):
                bitdict[res]=v
        return bitdict



s=Solution()

print(s.bitConvert("aaa"))

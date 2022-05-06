class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """


        res=""
        start=0
        while start<len(s):

            for i in range(k)[::-1]:
                if start+i<len(s):
                    res+=s[start+i]
            for i in range(k,2*k):
                if start+i<len(s):
                    res+=s[start+i]
            start+=2*k
        return res
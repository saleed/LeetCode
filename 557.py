class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        res=""
        i=0
        while i<len(s):
            if s[i].isalpha() or s[i]=="'":
                tmp=""
                while i<len(s) and  (s[i].isalpha() and  s[i]=="'"):
                    tmp+=s[i]
                    i+=1
                res+=tmp[::-1]
            else:
                res+=s[i]
                i+=1
        return res


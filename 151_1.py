class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        i=0
        tmpStr=""
        s+=" "#####notice this!!!!!!!!!!
        res=[]
        while i<len(s):
            if s[i]!=" ":
                tmpStr+=s[i]
            else:
                if tmpStr!="":
                    res.append(tmpStr)
                tmpStr=""
            i+=1
        return " ".join(list(reversed(res)))



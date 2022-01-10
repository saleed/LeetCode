class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        hashdict={}
        for v in strings:
            k=self.tokey(v)
            if k in hashdict:
                hashdict[k].append(v)
            else:
                hashdict[k]=[v]
        return list(hashdict.values())





    def tokey(self,s):
        for i in range(len(s)):
            delta=(ord(s[i])-ord('a')+26)%26
            s[i]=chr(ord(s[i])-delta+ord(a))
        return s
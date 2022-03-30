class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        hashdict={}
        for v in strings:
            k=self.getKey(v)
            if k in hashdict:
                hashdict[k].append(v)
            else:
                hashdict[k]=[v]


        res=[]
        for k in hashdict:
            res.append(hashdict[k])
        return res




    def getKey(self,str):
        intcode=""
        diff=ord(str[0])-ord('a')
        for v in str:
            intcode+=str(((ord(v)-diff-ord('a'))+26)%26)
        return intcode

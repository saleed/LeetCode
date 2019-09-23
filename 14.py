class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res=0
        if len(strs)==0:
            return ""
        while True:
            if self.samehead(strs,res):
                res+=1
                continue
            return strs[0][:res]


    def samehead(self,strs,i):
        if len(strs)==0:
            return False
        for s in strs:
            if len(s)-1<i or strs[0][i]!=s[i]:
                return False
        return True


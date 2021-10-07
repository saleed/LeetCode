class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)<=0:
            return ""
        i=0
        res=""
        while True:
            if len(strs[0])>i:
                ch=strs[0][i]
                for val in strs:
                    if len(val)>i and val[i]==ch:
                        continue
                    else:
                        return res
                res+=ch
            else:
                return res
            i+=1


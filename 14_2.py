class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res=""
        if len(strs)==0:
            return res
        p=0

        ch=""
        while True:
            for s in strs:
                if p<len(s):
                    if ch=="":
                        ch=s[p]
                    elif ch==s[p]:
                        continue
                    else:
                        return res
                else:
                    return res
            p+=1
            res+=ch
            ch=""





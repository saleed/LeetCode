class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        prefix=""
        i=0
        while True:
            tmp=""
            for j in range(len(strs)):
                if i>=len(strs[j]):
                    return prefix
                elif prefix=="":
                    prefix=strs[j][i]
                else:
                    if prefix==strs[j][i]:
                        continue
                    else:
                        return prefix
            i+=1
            prefix+=tmp

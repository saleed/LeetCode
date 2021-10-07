
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        res = ""
        i = 1
        while True:
            if len(strs) > 0 and i <= len(strs[0]):
                tmp_val = strs[0][:i]
            else:
                return res
            for val in strs:
                if val[:i] == tmp_val:
                    continue
                else:
                    return res
            res=tmp_val
            i += 1
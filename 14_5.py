class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        i = 0
        while True:
            if i < len(strs[0]):
                tmp = strs[0][i]
            else:
                break
            flag = 0
            for v in strs:
                if i < len(v) and v[i] == tmp:
                    continue
                else:
                    flag = 1
                    break
            if flag == 1:
                return prefix
            prefix += tmp
            i += 1
        return prefix


###代码非常不优雅
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        lt=str.split(" ")
        pat=list(pattern)
        if len(set(lt))!=len(set(pat)):
            return False
        dict={}
        for i in range(len(lt)):
            if lt[i] not in dict.keys():
                dict[lt[i]]=pat[i]
            elif lt[i] in dict.keys() and dict[lt[i]]!=pat[i]:
                return False

        return True

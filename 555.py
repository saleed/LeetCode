class Solution(object):
    def splitLoopedString(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        for i in range(len(strs)):
            if strs[i]<strs[i][::-1]:
                strs[i]=strs[i][::-1]

        maxstr="".join(strs)
        for i in range(len(strs)):
            midstr="".join(strs[i+1:]) + "".join(strs[:i])
            headstr=strs[i]
            for j in range(len(headstr)):
                newstr=headstr[j:]+midstr+headstr[:j]
                maxstr=max(maxstr,newstr)
            headstr=strs[i][::-1]
            for j in range(len(headstr)):
                newstr = headstr[j:] + midstr + headstr[:j]
                maxstr = max(maxstr, newstr)
        return maxstr



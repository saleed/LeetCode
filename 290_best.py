class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        slist=s.split(" ")
        chdict={}
        wordidct={}
        for i in range(len(pattern)):
            if pattern[i] not in chdict and slist[i] not in wordidct:
                chdict[pattern[i]]=slist[i]
                wordidct[slist[i]]=pattern[i]
            else:
                if pattern[i] in chdict and slist[i]==chdict[pattern[i]] and\
                        slist[i] in wordidct and  wordidct[slist[i]]!=pattern[i]:
                    continue
                else:
                    return False
        return True


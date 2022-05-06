class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """

        absday=0
        continueabsday=0
        for v in s:
            if v=="A":
                absday+=1
            elif v=="L":
                if continueabsday==3:
                    return False
                else:
                    continueabsday+=1
        return absday<2

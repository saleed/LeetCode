class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """

        lrdiff=[0,0]
        for i in range(len(s)):
            if s[i]==")":
                if lrdiff[1]==lrdiff[0]:
                    return False
                else:
                    lrdiff[1]-=1
                    lrdiff[0]=max(lrdiff[0]-1,0)
            elif s[i]=="(":
                lrdiff[0]+=1
                lrdiff[1]+=1
            else:
                lrdiff[0]=lrdiff[0]-1 if lrdiff[0]>0 else lrdiff[0]
                lrdiff[1]=lrdiff[1]+1

        return lrdiff[0]==0

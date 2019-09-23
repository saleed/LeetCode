class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dict={}
        for i in magazine:
            if i in dict.keys():
                dict[i]+=1
            else:
                dict[i]=1
        for j in ransomNote:
            if j in dict.keys() and dict[j]!=0:
                dict[j]-=1
            else:
                return False
        return True
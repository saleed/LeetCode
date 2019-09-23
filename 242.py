class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict={}
        for i in s:
            if i in dict.keys():
                dict[i]+=1
            else:
                dict[i]=1
        for j in t:
            if j in dict.keys():
                dict[j]-=1
            else:
                return False
        for key in dict.keys():
            if dict[key]!=0:
                return False
        return True
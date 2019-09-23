class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        strlist=str.split(' ')
        if len(pattern)!=len(strlist):
            return False
        for i in range(len(strlist)):
            strlist[i]='a'+strlist[i]
        dict={}
        for i in range(len(pattern)):
            if pattern[i] in dict.keys() and strlist[i] in dict.keys() and dict[pattern[i]]==dict[strlist[i]]:
                continue
            elif pattern[i] not in dict.keys() and strlist[i] not in dict.keys():
                dict[pattern[i]]=pattern[i]+strlist[i]
                dict[strlist[i]]=pattern[i]+strlist[i]
            else:
                return False
        return True

pattern = "abba"
str = "dog cat cat dog"

a=Solution()
print a.wordPattern(pattern,str)


#注意和最长公共字串LCS进行区分


#最长公共字串不要求一个字串中的所有字符在另外一个字符串中全部出现，LCS 找的是字符串中字母的公共部分




class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        p=0
        q=0
        while p<len(s) and q<len(t):
            if t[q]==s[p]:
                p+=1
            q+=1
        if q==len(t) and p<len(s):
            return False
        return True

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """





        vdict={}
        lmax=0
        pre_same_id=-1 ##更新左边界，左边界取遍历s的过程中遇到的相同值的最右位置
        for i in range(len(s)):
            if s[i] in vdict:
                pre_same_id=max(pre_same_id,vdict[s[i]])
            lmax=max(lmax,i-pre_same_id)
            vdict[s[i]]=i
        return lmax







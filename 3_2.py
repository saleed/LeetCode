#最长不重复子字符串
#方法1：最粗暴的方式，暴力的方法，复杂度O(n3)
#方法2：滑动窗口：
# 1.窗口的头尾指针初始指向0，
# 2.需要一个集合记录访问过的节点，同时要记录每个节点出现的位置，刚好上述两个操作合起来就是一个字典
# 3.不重复的时候就右边界右移，每次发现重复，就把窗口左边界逐位移动到到重复字符字符的位置+1，同时再移动的过程中更新字典，字典中删除经过的字符

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="":
            return 0
        dict={}
        start=0
        maxlen=1
        for end in range(len(s)):
            if s[end] not in dict.keys():
                dict[s[end]]=1
                maxlen=max(maxlen,end-start+1)
            else:
                while s[start]!=s[end]:
                    if dict[s[start]]==1:
                        del dict[s[start]]
                    else:
                        dict[s[start]]-=1
                    start+=1
                start+=1
        return maxlen





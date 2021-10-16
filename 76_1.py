###堆排序+滑动窗口


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        tset={}
        p=0
        q=0
        for v in t:
            if v not in  tset.keys():
                tset[v]=1
            else:
                tset[v]+=1

        tmpres={}
        while p<len(s) or q<len(s):



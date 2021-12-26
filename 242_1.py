# -*- coding: utf-8 -*

"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。


输入: s = "anagram", t = "nagaram"
输出: true

"""
#
# a="13452"
# b=list(a)
# b.sort()
# print(b)


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1=list(s)
        t1=list(t)
        s1.sort()
        t1.sort()

        return "".join(s1)=="".join(t1)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/14 10:51
# @Author  : sunaolin
# @File    : 208_5.py

##有两种实现方法，一种利用递归，一种是直接遍历字典树，递归代码比较简洁

class Trie(object):
    def __init__(self):
        self.wT={}
    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        tmpT=self.wT
        for v in word:
            if v in tmpT:
                continue
            else:
                tmpT[v]={}
                tmpT=tmpT[v]
        tmpT["#"]=1


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        tmpT=self.wT
        for v in word:
            if v in tmpT:
                tmpT=tmpT[v]
            else:
                return False
        return "#" in tmpT


    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        tmpT = self.wT
        for v in prefix:
            if v in tmpT:
                tmpT = tmpT[v]
            else:
                print(v)
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
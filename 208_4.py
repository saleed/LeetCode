#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/5 15:05
# @Author  : sunaolin
# @File    : 208_4.py


class Trie(object):
    def __init__(self):
        self.tree={}



    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        if len(word)==0:
            self.tree[""]=1
            return
        if word[0] in self.tree:
            self.tree[word[0]].insert(word[1:])
        else:
            self.tree[word[0]]=Trie()
            self.tree[word[0]].insert(word[1:])


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word)==0 and "" in  self.tree:
            return True
        if len(word)>0:
            if word[0] in self.tree and self.tree[word[0]].search(word[1:]):
                return True
        return False


    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        if len(prefix)==0:
            return True
        if len(prefix)>0:
            if prefix[0] in self.tree and self.tree[prefix[0]].startsWith(prefix[1:]):
                return True
        return False



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
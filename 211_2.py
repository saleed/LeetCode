#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/6 13:54
# @Author  : sunaolin
# @File    : 211_2.py

class WordDictionary(object):

    def __init__(self):
        self.dict={}


    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        if word=="":
            self.dict["#"]=1
            return
        if word[0] in self.dict:
            self.dict[word[0]].addWord(word[1:])
        else:
            self.dict[word[0]]=WordDictionary()
            self.dict[word[0]].addWord(word[1:])



    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word=="" and "#" in self.dict:
            return True
        elif word!="":
            if word[0]==".":
                for k in self.dict:
                    if k=="#":
                        continue
                    if self.dict[k].search(word[1:]):
                        return True
            else:
                if word[0] in self.dict and self.dict[word[0]].search(word[1:]):
                    return True
        return False



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/7 17:22
# @Author  : sunaolin
# @File    : 676——1.py


class MagicDictionary(object):

    def __init__(self):
        self.dict={}


    def buildDict(self, dictionary):
        """
        :type dictionary: List[str]
        :rtype: None
        """
        for v in dictionary:
            self.add(v)



    def search(self, searchWord):
        """
        :type searchWord: str
        :rtype: bool
        """
        return self.searchNum(searchWord,1)


    def searchNum(self,word,num):
        if word=="":
            if "#" in self.dict and num==0:
                return True
            else:
                return False
        else:

            for k in self.dict:
                if k=='#':
                    continue
                if k==word[0]:
                    if self.dict[k].searchNum(word[1:],num):
                        return True
                else:
                    if num > 0 and self.dict[k].searchNum(word[1:],num-1):
                        return True
            return False


    def add(self,word):
        if word=="":
            self.dict["#"]=1
            return
        if word[0] in self.dict:
            self.dict[word[0]].add(word[1:])
        else:
            self.dict[word[0]]=MagicDictionary()
            self.dict[word[0]].add(word[1:])




# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
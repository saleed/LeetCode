#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/15 15:30
# @Author  : sunaolin
# @File    : 737)1.py





class Solution(object):
    def areSentencesSimilarTwo(self, sentence1, sentence2, similarPairs):
        """
        :type sentence1: List[str]
        :type sentence2: List[str]
        :type similarPairs: List[List[str]]
        :rtype: bool
        """
        if len(sentence1)!=len(sentence2):
            return False

        uf=UnionFind()

        for v in similarPairs:
            uf.merge(v[0],v[1])

        for i in range(len(sentence1)):
            if uf.findRoot(sentence1[i])==uf.findRoot(sentence2):
                continue
            return False
        return True










class UnionFind:
    def __init__(self):
        self.vdict={}


    def add(self,k):
        if k not in self.vdict:
            self.vdict[k]=k
    def merge(self,k1,k2):
        self.add(k1)
        self.add(k2)
        self.vdict[self.findRoot(k1)]=self.findRoot(k2)

    def findRoot(self,k):
        if k!=self.vdict[k]:
            return self.findRoot(self.vdict[k])
        return k

    def sameRoot(self,k1,k2):
        return self.findRoot(k1)==self.findRoot(k2)

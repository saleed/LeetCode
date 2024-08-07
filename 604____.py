#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/3 10:23
# @Author  : sunaolin
# @File    : 604.py


class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.compress=compressedString
        self.id=-1
        self.num=0
        self.cnt=0


    def next(self):
        """
        :rtype: str
        """

        ret=" "

        if self.cnt<self.num:
            self.cnt+=1
            return self.compress[self.id]
        if self.cnt==self.num:
            self.id += 1
            while self.id<len(self.compress) and not self.compress[self.id].isalpha():
                self.id+=1
            d=""
            i=self.id+1
            while i<len(self.compress) and self.compress[i].isdigit():
                d+=self.compress[i]
                i+=1
            if self.id>=len(self.compress): ##
                return " "
            self.cnt=1
            print(d)
            try:
                self.num=int(d)
            except:
                print(self.id,i,d)
            # return self.compress[self.id]
            print(self.id,self.num,self.cnt)
            return self.compress[self.id]
        return ret


    def hasNext(self):
            """
            :rtype: bool
            """
            if self.cnt < self.num:
                return True
            else:
                i = self.id+1
                while i < len(self.compress) and not self.compress[i].isalpha():
                    i += 1
                return i<len(self.compress)



# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
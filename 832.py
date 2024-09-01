#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/29 14:29
# @Author  : sunaolin
# @File    : 832.py


class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """

        for i in range(len(image)):
            for j in range(int((len(image[0])+1)/2)):
                tmp=image[i][j]
                if image[i][len(image[0])-1-j]==0:
                    image[i][j]=1
                else:
                    image[i][j]=0
                if tmp==1:
                    image[i][len(image[0]) - 1 - j]=0
                else:
                    image[i][len(image[0]) - 1 - j]= 1


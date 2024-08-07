#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/31 20:43
# @Author  : sunaolin
# @File    : 558_1.py


"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution(object):
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        if quadTree1==None or quadTree2==None:
            return None
        if quadTree1.isLeaf:
            if quadTree1.val==0:
                return quadTree2
            else:
                return quadTree1
        elif quadTree2.isLeaf:
            if quadTree2.val==0:
                return quadTree1
            else:
                return quadTree2
        else:
            ret = Node(0, False)
            ret.topLeft = self.intersect(quadTree1.topLeft,quadTree2.topLeft)
            ret.topRight = self.intersect(quadTree1.topRight,quadTree2.topRight)
            ret.bottomLeft = self.intersect(quadTree1.bottomLeft,quadTree2.bottomLeft)
            ret.bottomRight = self.intersect(quadTree1.bottomRight,quadTree2.bottomRight)
            if (ret.topLeft.isLeaf==1 and ret.topLeft.val==1) and (ret.bottomLeft.isLeaf==1 and ret.bottomLeft.val==1) and \
                    (ret.topRight.isLeaf==1 and ret.topRight.val==1) and (ret.bottomRight.isLeaf==1 and ret.bottomRight.val==1):
                return Node(1,True)
            return ret
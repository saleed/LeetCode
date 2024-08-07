#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/10 21:28
# @Author  : sunaolin
# @File    : 297)_1.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        row=[root]
        res=[]
        while len(row)>0:
            nrow=[]
            for v in row:
                if v==None:
                    res.append(None)
                else:
                    res.append(v.val)
                    nrow.append(v.left)
                    nrow.append(v.right)
            # print(res)
            # break
            row=nrow
        # print(res)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data)==0:
            return None
        row=[TreeNode(data[0])]
        root=row[0]
        p=1
        while len(row)>0:
            nrow=[]
            for v in row:
                if v==None:
                    continue
                lNode=None if data[p]==None else TreeNode(data[p])
                v.left=lNode
                nrow.append(lNode)
                p+=1
                rNode = None if data[p] == None else TreeNode(data[p])
                v.right=rNode
                nrow.append(rNode)
                p+=1
            row=nrow
        print(root)
        return root






# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
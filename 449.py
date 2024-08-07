#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/22 22:39
# @Author  : sunaolin
# @File    : 449.py

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
        if root==None:
            return ""
        res=str(root.val)
        return res+"("+self.serialize(root.left)+")"+"("+self.serialize(root.right)+")"

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        print(data)
        if len(data)==0:
            return None
        i=0

        tmp=""
        while i<len(data) and data[i].isdigit():
            tmp+=data[i]
            i+=1
        st=1
        # print(tmp)
        root=TreeNode(int(tmp))
        i+=1
        lstart=i
        while i<len(data) and st>0:
            if data[i]==")":
                st-=1
            elif data[i]=="(":
                st+=1
            i+=1
        lend=i-2
        if lend<len(data):
            root.left=self.deserialize(data[lstart:lend+1])
        i+=1
        rstart = i
        st=1
        while i < len(data) and st > 0:
            if data[i] == ")":
                st -= 1
            elif data[i] == "(":
                st += 1
            i += 1
        rend = i - 2
        if rend<len(data):
            root.right=self.deserialize(data[rstart:rend+1])
        return root







# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
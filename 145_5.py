#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/8 23:35
# @Author  : sunaolin
# @File    : 145_5.py


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        st=[]
        p=root
        res=[]
        ##后续遍历的难点在于判断st中的节点是否访问过右子树，所以增加一个标志判断
        while p or len(st)>0:
            while p:
                st.append([p,0])
                p=p.left
            top=st[-1]
            if top[1]==1 or top[0].right==None:
                res.append(top[0].val)
                st.pop()
            else:
                st[-1][1]=1
                p=st[-1][0].right
        return res


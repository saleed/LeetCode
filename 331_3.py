#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/15 12:31
# @Author  : sunaolin
# @File    : 331-3.py

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stat=0
        st=[]
        for v in preorder:
            if stat==0:
                if v=="#":
                    stat=1
                else:
                    st.append(v)
            else:
                if len(st)==0:   ###这里判断遇到#的时候是否有根节点
                    return False
                st.pop()  ##当stat=1 的时候，下一个一定是根节点右子树，根节点已经合法，弹出根节点
                if v!="#":  ##发现
                    st.append(v)
        return True

###如果是中序遍历呢





##层次遍历编码的判断是否合法
    def layer(self,preorder):
        if len(preorder)==0:
            return True
        layer=[preorder[0]]
        i=1
        while len(layer)>0:
            nlayer=[]
            for v in layer:
                if v=="#":
                    continue
                else:
                    if i+1>=len(preorder):
                        return False
                    nlayer.append(preorder[i])
                    nlayer.append(preorder[i+1])
                    i+=1
            layer=nlayer
        return True


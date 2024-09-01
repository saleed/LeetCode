#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/29 21:12
# @Author  : sunaolin
# @File    : 841.py


class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        keys=rooms[0]
        vis=set()
        self.dfs(rooms,keys,vis)
        if len(vis)==len(rooms):
            return True
        return False


    def dfs(self,rooms,keys,vis):
        if len(keys)==0:
            return
        if keys[0] not in vis:
            vis.add(keys[0])
            keys=keys[1:]+rooms[keys[0]]
        else:
            keys=keys[1:]

        self.dfs(rooms,keys,vis)


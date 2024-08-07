#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/25 22:11
# @Author  : sunaolin
# @File    : 499_1.py

class Solution(object):
    def findShortestWay(self, maze, ball, hole):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str
        """
        path={}
        res=self.dfs(maze,set(),path,ball[0],ball[1],hole)
        print(path)
        return "impossible" if res=="z"*100 else res
        # return res

####最短距离！！！！！不是最短路径
    def dfs(self,maze,vis,path,xs,ys,hole): ##path用来记录更新全局最小值，vis用于记录一次dfs中访问过的节点
        if (xs,ys) in path:
            return path[(xs,ys)]

        invalid= "z"*100
        print(xs,ys)
        if (xs,ys) in vis:
            return invalid

        path[(xs, ys)] =invalid
        x=xs
        y=ys
        flag=0
        while 0<=x+1<len(maze) and maze[x+1][y]==0:
            x+=1
            if x == hole[0] and y == hole[1]:
                flag=1
                break

        if not flag:
            vis.add((xs, ys))
            ret= self.dfs(maze,vis,path,x,y,hole)
            vis.remove((xs, ys))
            if ret!=invalid:
                tmp="d" + ret
                # path[(xs, ys)] = min(path[(xs, ys)],tmp)
                if len(path[(xs,ys)])>len(tmp) or (len(path[(xs,ys)])==len(tmp) and path[(xs,ys)]>tmp):
                    path[(xs,ys)]=tmp
        else:
            path[(xs, ys)] = min(path[(xs, ys)], "d")

        x = xs
        y = ys
        flag = 0
        while 0 <= y - 1 < len(maze[0]) and maze[x][y - 1] == 0:
            y -= 1
            if x == hole[0] and y == hole[1]:
                flag = 1
                break
        if not flag:
            vis.add((xs, ys))
            ret = self.dfs(maze, vis, path, x, y, hole)
            vis.remove((xs, ys))
            if ret != invalid:
                tmp = "l" + ret
                # path[(xs, ys)] = min(path[(xs, ys)], tmp)
                if len(path[(xs, ys)]) > len(tmp) or (len(path[(xs, ys)]) == len(tmp) and path[(xs, ys)] > tmp):
                    path[(xs,ys)]=tmp
                # return path[(xs, ys)]
        else:
            path[(xs, ys)] = min(path[(xs, ys)], "l")

        x = xs
        y = ys
        flag=0
        while 0 <= y + 1 < len(maze[0]) and maze[x][y+1]==0:
            y += 1
            if x == hole[0] and y == hole[1]:
                flag = 1
                break

        if not flag:
            vis.add((xs, ys))
            ret= self.dfs(maze, vis,path, x, y, hole)
            vis.remove((xs, ys))

            if ret !=invalid:
                tmp = "r" + ret
                # path[(xs, ys)] = min(path[(xs, ys)], tmp)
                if len(path[(xs, ys)]) > len(tmp) or (len(path[(xs, ys)]) == len(tmp) and path[(xs, ys)] > tmp):
                    path[(xs, ys)] = tmp

        else:
            path[(xs, ys)] = min(path[(xs, ys)], "r")

        x = xs
        y = ys
        res=[]
        while 0 <= x-1< len(maze)and maze[x-1][y]==0:
            x -= 1
            if x == hole[0] and y == hole[1]:
                res.append("u")
                flag = 1
                break

        if not flag:
            vis.add((xs, ys))
            ret=self.dfs(maze,vis, path, x, y, hole)
            vis.remove((xs, ys))
            if ret != invalid:
                tmp = "u" + ret
                path[(xs, ys)] = min(path[(xs, ys)], tmp)
                if len(path[(xs, ys)]) > len(tmp) or (len(path[(xs, ys)]) == len(tmp) and path[(xs, ys)] > tmp):
                    path[(xs, ys)] = tmp
                # return path[(xs, ys)]
        else:
            path[(xs, ys)] = min(path[(xs, ys)], "u")
            # return path[(xs, ys)]

        return path[(xs, ys)]

maze =[[0,0,0,0,0,0,0],[0,0,1,0,0,1,0],[0,0,0,0,1,0,0],[0,0,0,0,0,0,1]]
for v in maze:
    print(v)
ball =[0,4]
hole =[3,5]
a=Solution()
print(a.findShortestWay(maze,ball,hole))
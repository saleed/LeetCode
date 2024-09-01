#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/26 10:07
# @Author  : sunaolin
# @File    : 800.py


class Solution(object):
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        color = color[1:]
        return "#" + self.getCloset(color[:2]) + self.getCloset(color[2:4]) + self.getCloset(color[4:])

    def getCloset(self, oxstr):
        mindist = float("inf")
        res = ""
        ox1 = ""
        if oxstr[0] != '0':
            print(oxstr[0])
            ox1 = str(int(oxstr[0], 16) - 1) * 2
        ox2 = ""
        if oxstr[0] != "f":
            ox2 = str(int(oxstr[0], 16) + 1) * 2
        ox3 = min(oxstr[0], oxstr[1]) * 2
        ox4 = max(oxstr[0], oxstr[1]) * 2
        print(ox1, ox2, ox3, ox4, oxstr)
        if ox1 != "" and abs(int(ox1, 16) - int(oxstr, 16)) < mindist:
            print(abs(int(ox1, 16) - int(oxstr, 16)))
            mindist = ox1
            res = ox1
        if ox2 != "" and abs(int(ox2, 16) - int(oxstr, 16)) < mindist:
            print( abs(int(ox2, 16) - int(oxstr, 16)))
            mindist = ox2
            res = ox2
        if abs(int(ox3, 16) - int(oxstr, 16)) < mindist:
            print(abs(int(ox3, 16) - int(oxstr, 16)))
            mindist = ox3
            res = ox3
        if abs(int(ox4, 16) - int(oxstr, 16)) < mindist:
            print(abs(int(ox4, 16) - int(oxstr, 16)))
            mindist = ox4
            res = ox4
        return res
#
# print(str(int('f', 16) - 1) * 2)
# print(('f', 16) - 1)

print(str(hex(15)))
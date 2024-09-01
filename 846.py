#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/31 14:33
# @Author  : sunaolin
# @File    : 846.py


class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        g = 0
        gnum = len(hand) / groupSize
        while g < gnum:
            # print(hand)
            cnt = 1
            i = 1
            tmp = hand[0]
            while i < len(hand):
                if cnt == groupSize:###这里要写到前面，因为之前tmp=1,i=1相当于已经统计过一次cnt
                    break
                if hand[i] == tmp + 1:
                    cnt += 1
                    tmp += 1

                i += 1
            if cnt != groupSize:
                return False
            tmp = hand[0]
            for i in range(groupSize):
                hand.remove(tmp + i)
                # print(hand)

            g += 1
        return True


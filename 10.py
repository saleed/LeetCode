#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/18 14:14
# @Author  : sunaolin
# @File    : 10.py


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.match(s,p)

    def match(self,s,p):
        print(s,p)
        if len(s)==0 and len(p)==0:
            return True
        elif len(p)>0:
            if len(p)>1 and p[1]=="*":
                if self.match(s,p[2:]):
                    # print(s,p)
                    return True
                # print(s,p)b
                # base=s[0]
                for i in range(len(s)):
                    if s[i]==p[0] or (p[0]=="." ):
                        # print(s[i+1:],p[2:])
                        if self.match(s[i+1:],p[2:]):
                            # print("11",s[i+1:],p[2:])
                            return True
                    else:
                        break
                return False
            elif p[0]==".":
                return self.match(s[1:],p[1:])
            else:
                if len(s)>0 and s[0]==p[0]:
                    return self.match(s[1:],p[1:])
                return False
        return False


a=Solution()
s=u'ssippi'
p=u'p*.'
print(a.match(s,p))
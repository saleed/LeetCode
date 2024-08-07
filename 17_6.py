# -*- coding: utf-8 -*-
# @Author : 孙奥林
# @Time : 7/5/2024 下午11:16


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dlist = [str(i) for i in range(2, 10)]
        vlist = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        dmap = dict(zip(dlist, vlist))


        # return self.dfsBottom2Top(digits, dmap)
        # return self.dfsTop2Bottom([],digits,0,dmap)

        if digits=="":
            return []
        res=[]
        self.dfsTop2BottomBy(res,digits,0,dmap,"")
        return res




    ##自底朝上归约结果
    def dfsBottom2Top(self,digit,dmap):
        if digit=="":
            return []
        first=digit[0]
        ret=self.dfs(digit[1:],dmap) ##
        if len(ret)==0:
            return list(dmap[first])
        newres=[]
        for c in dmap[first]:
            for v in ret:
                newres.append(c+v)
        return newres

    ###自顶朝下，记录中间结果，错误的写法，想中间记录1-i的所有组合为res 中间修改res res无法保存
    # 但是记录
    def dfsTop2Bottom(self,res,digit,i,dmap):
        if i>=len(digit):
            return res
        if len(res)==0:
            res=list(dmap[digit[i]])
            return self.dfsTop2Bottom(res,digit,i+1,dmap)
        else:
            newres=[]
            for v in res:
                for c in dmap[digit[i]]:
                    newres.append(v+c)
            return self.dfsTop2Bottom(newres,digit,i+1,dmap)


    def dfsTop2BottomBy(self,res,digit,i,dmap,tmpstr):
        if i==len(digit):
            res.append(tmpstr)
            return
        for c in dmap[digit[i]]:
            newstr=tmpstr+c
            self.dfsTop2BottomBy(res,digit,i+1,dmap,newstr)
print(list("abcde"))
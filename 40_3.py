class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candi_dic={}
        for v in candidates:
            if v in candi_dic.keys():
                candi_dic[v]+=1
            else:
                candi_dic[v]=1
        leftkey=candi_dic.keys()
        self.dfs(candi_dic, target, res, [],leftkey)
        return res


    def dfs(self,candi_dic,target,res,cur,leftkey):
        # print(candicate,i,target,cur)
        if target==0:
            res.append(cur[:])
        if target>0 and len(leftkey)>0:
            for i in range(candi_dic[leftkey[0]]+1):
                newcur=cur[:]
                newcur.extend(i*[leftkey[0]])
                new_left=leftkey[1:]
                self.dfs(candi_dic,target-i*leftkey[0],res,newcur,new_left)



candidates=[10,1,2,7,6,1,5]
target =8
a=Solution()
print(a.combinationSum2(candidates,target))

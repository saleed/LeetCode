class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        id=0
        left=target
        res=[]
        cursel=[]
        self.dfs(candidates,id,left,res,cursel)
        return res


    def dfs(self,candidate,id,left,res,cursel):
        if left==0:
            res.append(cursel[:])
            return
        elif left>0 and id<len(candidate):
            k=0
            while left-k*candidate[id]>=0:  #大于等于！！！
                newsel=cursel[:]
                newsel.extend(k*[candidate[id]])
                # print(newsel)
                self.dfs(candidate,id+1,left-k*candidate[id],res,newsel)
                k+=1
        else:
            return



# test=[1,2]
# test.extend([1]*0)
# print(test)

# candidates = [2,3,6,7]
# target = 7
# a=Solution()
# print(a.combinationSum(candidates,target))

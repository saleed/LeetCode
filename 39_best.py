class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs(candidates,target,0,[],res,0)
        return res

    def dfs(self,candidate,target,tmpsum,tmpsel,res,i):
        if tmpsum==target:
            res.append(tmpsel[:])
            return
        if i<len(candidate):
            num=0
            while tmpsum+num*candidate[i]<=target:
                tmpsel.extend([candidate[i]]*num)
                self.dfs(candidate,target,tmpsum+num*candidate[i],tmpsel,res,i+1)
                tmpsel=tmpsel[:len(tmpsel)-num]
                num+=1


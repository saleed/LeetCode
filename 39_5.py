class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res=[]
        self.dfs(candidates,0,target,res,[])
        return res


    def dfs(self,candicate,i,target,res,cur):
        # print(candicate,i,target,cur)
        if target==0:
            res.append(cur[:])
        if target>0 and i<len(candicate):
            n=0
            while n*candicate[i]<=target:
                newcur=cur[:]
                newcur.extend(n*[candicate[i]])
                self.dfs(candicate,i+1,target-n*candicate[i],res,newcur)
                n+=1


if __name__ == "__main__":
    a=Solution()
    test=[2,3,6,7]
    target=7
    print(a.combinationSum(test,7))
    # print(test)
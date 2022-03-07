class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        hashset=dict()
        for v in candidates:
            if v in hashset:
                hashset[v]+=1
            else:
                hashset[v]=1

        res=[]
        self.dfs(target,hashset,res,[],0)
        return res



    def dfs(self,target,hashset,res,tmpsel,tmpsum):
        # print(len(tmpsel),tmpsel,hashset)
        if tmpsum==target:

            res.append(tmpsel[:])
            # print(hashset)
            return
        if tmpsum<target:
            key=hashset.keys()
            for k in key:
                if hashset[k]==0:
                    continue
                num=hashset[k]
                hashset[k] = 0
                # print(hashset)
                for n in range(num+1):
                    tmpsel.extend(n*[k])
                    self.dfs(target,hashset,res,tmpsel,tmpsum+k*n)
                    tmpsel=tmpsel[:len(tmpsel)-n]
                hashset[k] = num
                break



a=Solution()
test=[10,1,2,7,6,1,5]
target=8


print(a.combinationSum2(test,target))
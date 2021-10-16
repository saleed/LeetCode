class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """


        numdic={}
        for v in nums:
            if v in numdic.keys():
                numdic[v]+=1
            else:
                numdic[v]=1
        res=[]
        self.dfs(numdic,res,[])
        return res


    def dfs(self,numdic,res,cur):
        if len(numdic)==0:
            res.append(cur[:])
            return
        for k in numdic.keys():
            n=numdic[k]
            del numdic[k]
            for v in range(n+1):
                newcur=cur[:]
                newcur.extend([k]*v)
                self.dfs(numdic,res,newcur)
            numdic[k]=n
            break
nums = [1,2,2]
a=Solution()
print(a.subsetsWithDup(nums))
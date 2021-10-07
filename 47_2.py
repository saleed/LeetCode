class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs(res,[],nums)
        return res



    def dfs(self,res,tmp,left):
        if len(left)==0:
            res.append(tmp[:])
            return
        leftset=set(left)
        for val in leftset:
            tmp.append(val)
            newleft=left[:]
            newleft.remove(val)
            self.dfs(res,tmp,newleft)
            tmp.pop()

if __name__=="__main__":
    a=Solution()
    test=[1,1,2,2]

    print(a.permuteUnique(test))
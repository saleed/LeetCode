class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        left=nums[:]
        self.dfs(res,[],left)
        return res



    def dfs(self,res,tmp,left):
        if len(left)==0:
            res.append(tmp[:])
            return
        for val in left:
            tmp.append(val)
            new_left=left[:]
            new_left.remove(val)
            self.dfs(res,tmp,new_left)
            tmp.remove(val)

if __name__=="__main__":
    a=Solution()
    test=[1,2,3,4]
    print(a.permute(test))
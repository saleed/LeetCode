class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        treeList=self.buildTree(nums)
        res=self.dfs(treeList,1)
        return sum(res)


    def dfs(self,tree,i):
        if tree[i]==float("inf"):
            return []
        if tree[2*i]==float("inf") and tree[2*i+1]==float("inf"):
            return [tree[i]]
        else:
            left=self.dfs(tree,2*i)
            right=self.dfs(tree,2*i+1)
            res=[]
            for v in left:
                res.append(v+tree[i])
            for v in right:
                res.append(v+tree[i])
            return res




    def buildTree(self,nums):
        if len(nums)==0:
            return None

        tree=[0]*float("inf")
        for v in nums:
            d=v/100
            p=v/10%10
            val=v%10
            start=math.pow(2,d-1)
            tree[start+p-1]=val
        return tree




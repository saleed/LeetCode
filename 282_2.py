class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """








    #递归思路，给定一个nums 从nums中选出来左操作数，和左操作数对右边的符号
    def dfs(self,nums,target):
        if len(nums)==0:
            return []
        if int(nums)==target:
            return [int(nums)]
        res=[]
        for i in range(len(nums)):
            left=nums[:i+1]
            add=self.dfs(nums[i+1:],target-int(left))
            minus=self.dfs(nums[i+1:],int(left)-target)
            for m in add:
                res.append(left+'+'+m)
            for n in minus:
                res.append(left+'-'+n)-



class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ##寻找拓扑排序的起点

        notvis=[i for i in range(len(nums))]
        for i in range(len(nums)):
            if nums[i]<len(nums):
                notvis.remove(nums[i])

        ###1.首先找到可能的起点
        dist={}
        maxl=0
        for i in notvis:
            pos=i
            l=0
            ##2.剪枝
            while nums[pos] <len(nums) and ((nums[pos] not in dist or dist[nums[pos]]<l)):
                dist[nums[pos]]=l
                pos=nums[pos]
            maxl=max(maxl,l)
        return maxl




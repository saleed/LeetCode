#use queue to solve this querstion

#this question can be abstracted as a graph


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach=[0]*len(nums)
        reach[0]=1
        maxid=0
        for i in range(len(nums)-1):

            if i+nums[i]>maxid:
                maxid=i+nums[i]

        print(maxid)
        return maxid>=len(nums)-1



tt=[2,3,1,1,4]
a=Solution()
print(a.canJump(tt))
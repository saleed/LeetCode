class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ############二分的方法：
        ###:分治的方法

        ##
        if len(nums)==1:
            return nums[0]
        left=0
        right=len(nums)-1

        while left<right:
            mid=int((left+right)/2)
            if nums[mid]<nums[right]: ###必须是判断mid和right 因为可能出现在整体升序的情况 这样判断仍然适用
                ##分析：这里不可能有等于号，因为mid和right一定不等，且没有重复元素
                #如果有重复元素：
                #[1,3,3] 这个用例会有问题，如果判断条件加上等于
                #则# [3,3,1,3]这个用例同样会有问题
                right=mid  ###考虑好边界
            else:
                left=mid+1
        return nums[left]
a=Solution()
nums=[3,4,5,1,2]
print(a.findMin(nums))
nums=[4,5,6,7,0,1,2]
print(a.findMin(nums))
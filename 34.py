class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        flag=0
        start=-1
        end=-1
        for i in range(len(nums)):
            if nums[i]==target:
                if not flag:
                    flag=1
                    start=i
                    end=i
                else:
                    end=i
            else:
                flag=0

        return [start,end]


a=Solution()


nums = [5,7,7,8,8,10]
target = 8
# 输出: [3,4]
print(a.searchRange(nums,target))


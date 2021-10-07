## coding:UTF-8


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binary(nums,target)



    def binary(self,nums,target):
        p=0
        q=len(nums)-1

        ##如果p<=q 更新时候要p=mid+1 q=mid-1 如果是p<q p=mid+1 q=mid即可
        ##一定要保证边界条件可以跳出
        while p<=q:
            print(p,q)
            mid=(p+q)/2
            if nums[mid]==target:
                return mid

            ###下面这个判断的等号非常重要？？？？为什么想不通
            if nums[mid]>=nums[p]:
                if nums[p] <= target < nums[mid]:
                    q=mid-1
                else:
                    p=mid+1
            else:
                if nums[q] >= target > nums[mid]:
                    p=mid+1
                else:
                    q=mid-1

        return -1


a=Solution()
nums = [4,5,6,7,0,1,2]
target = 2
# nums = [3,1]
# target = 1
print(a.search(nums,target))


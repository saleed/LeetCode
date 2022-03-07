## coding:UTF-8


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        p=0
        q=len(nums)-1

        while p<=q:  ##binary search is left bound <= right bound
            mid=(p+q)/2
            if nums[mid]==target:
                return mid
            if nums[mid]<=nums[q]:
                if target>=nums[mid] and target<=nums[q]:
                    p=mid+1
                else:
                    q=mid-1
            else:
                if target<=nums[mid] and target>=nums[p]:
                    q=mid-1
                else:
                    p=mid+1  ###p=mid then the code will not jump out the while
        return -1
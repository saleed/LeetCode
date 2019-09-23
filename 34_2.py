class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s=0
        e=len(nums)

        start=-1
        end=-1
        while s<=e:
            if s==e and target==nums[s]:
                start=s
                break
            mid=int((s+e)/2)
            if s[mid]<target:
                s=mid+1
            elif s[mid]>target:
                e=mid-1
            else:
                e=mid-1


        while s<=e:
            if s==e and target==nums[s]:
                end=s
                break
            mid=int((s+e)/2)
            if s[mid]<target:
                s=mid+1
            elif s[mid]>target:
                e=mid-1
            else:
                s=s+1

        return [start,end]





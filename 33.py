class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return -1
        if len(nums)==1 and nums[0]==target:
            return 0
        s=0
        e=len(nums)-1
        while s<=e: #####注意！！！！ 二分法要点,一定是等于！！！！如果是小于的
            print(s,e)
            mid=int((s+e)/2)
            if nums[mid]==target:
                return mid
            if nums[mid]<nums[e]:
                if target<=nums[e] and target>nums[mid]:
                    s=mid+1  ###二分法要点2，左边界一定是mid+1，更新右边界可以是mid!!!!!
                else:
                    e=mid
            else:
                if target<nums[mid] and target>=nums[s]:
                    e=mid
                else:
                    s=mid+1
        return -1




    def binarySearch(self,nums,target):

        if len(nums)==0:
            return -1

        p=0
        q=len(nums)-1

        while p<=q:
            mid=int((p+q)/2)

            if nums[mid]==target:
                return mid
            if nums[p]<=nums[mid]:
                if target<=a[mid] and target>=a[p]:
                    q=mid
                else:
                    p=mid+1
            else:
                if target<=nums[q] and target>=nums[mid]:
                    p=mid+1
                else:
                    q=mid
        return -1


a=Solution()

nums=[4, 5, 6, 7, 0, 1, 2]
target=0

print(a.search(nums,target))
nums=[1,3]
print(a.search(nums,3))



p+q)/2
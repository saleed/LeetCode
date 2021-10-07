#2021801###审题不清
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        p=0
        q=len(nums)-1
        while p<q:
            sumVal=nums[p]+nums[q]
            if sumVal<target:
                p+=1
            elif sumVal>target:
                q-=1
            else:
                return [p,q]


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_set={}
        for i in range(len(nums)):
            if nums[i] in num_set.keys():
                num_set[nums[i]].append(i)
            else:
                num_set[nums[i]]=[i]

        for val in nums:
            if target-val in num_set.keys():
                if 2*val==target:
                    if len(num_set[val])>=2:
                        return num_set[val][:2]
                else:
                    return [num_set[val][0],num_set[target-val][0]]





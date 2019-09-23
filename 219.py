class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict={}
        for i in range(len(nums)):
            if dict.has_key(nums[i]):
                for j in dict[nums[i]]:
                    if abs(j-i)<=k:
                        return True
                dict[nums[i]].append(i)
            else:
                dict[nums[i]]=[i]
        return False


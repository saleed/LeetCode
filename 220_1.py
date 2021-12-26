class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """

        s=set()

        minv=float("inf")
        maxv=-float("inf")

        for i in nums[:k+1]:
            s
            if nums[i] in s:
                return False
            s.add(nums[i])
        p=k+1
        while p<len(nums):
            rmv=nums[p-(k+1)]
            s.remove(rmv)
            if nums[p] in s:
                return False

            if rmv==minv or rmv==maxv:
                minv = float("inf")
                maxv = -float("inf")
                for i in range(p-k,p+1):
                    minv = min(minv, nums[i])
                    maxv = max(maxv, nums[i])
                if abs(maxv-minv)>t:
                    return False



#2021801
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return self.solve2(nums,target)

    def solve1(self,nums,target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return [-1,-1]

    def solve2(self,nums,target):
        hashset=dict()
        for i in range(len(nums)):
            if nums[i] in hashset.keys():
                hashset[nums[i]].append(i)
            else:
                hashset[nums[i]]=[i]
        for v in nums:
            if target-v!=v and target-v in hashset.keys():
                return [hashset[v][0],hashset[target-v][0]]
            if target-v==v and len(hashset[v])>=2:
                return [hashset[v][0],hashset[v][1]]
        return [-1,-1]
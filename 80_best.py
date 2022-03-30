class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=0
        p=0
        pre=float("inf")
        for i in range(len(nums)):
            if nums[i]==pre:
                if n==2:
                    continue
                else:
                    n+=1
                    nums[p]=nums[i]
                    p+=1
            else:
                n=1
                nums[p]=nums[i]
                p+=1
            pre=nums[i]

        return p

a=Solution()
test=[1,1,1,2,2,3]
print(a.removeDuplicates(test))
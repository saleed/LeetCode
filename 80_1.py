class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        prech=""
        prenum=0

        p=0
        for i in range(len(nums)):
            if nums[i]!=prech:
                prech=nums[i]
                prenum=1
                nums[p]=prech
                p+=1
            elif prenum<=1:
                prenum+=1
                nums[p]=prech
                p+=1
            else:
                prenum+=1

        return nums[:p]
tst=[0,0,0,1,1,1,1,2,3,3]
a=Solution()
print(a.removeDuplicates(tst))

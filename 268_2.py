class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        summ=sum(nums)
        n=len(nums)
        norm=int((n*(n-1))/2)
        # print(summ,norm)
        return n-(summ-norm)


a=Solution()
t=[1,0,3]
print(a.missingNumber(t))
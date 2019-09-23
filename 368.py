class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)==0:
            return []
        dict=[1]*len(nums)
        pre=[-1]*len(nums)
        nums.sort()
        for i in range(len(nums)):
            p=i-1
            while p>=0:
                if nums[i]%nums[p]==0 and dict[i]<dict[p]+1:
                    dict[i]=dict[p]+1
                    pre[i]=p
                p-=1
        maxv=-float("inf")
        id=0
        for i in range(len(dict)):
            if maxv<dict[i]:
                id=i
                maxv=dict[i]
        res=[]
        print dict,pre
        print id
        while id>=0:
            res=[nums[id]]+res
            id=pre[id]
        return res

In= [1,2,3]
a=Solution()
print a.largestDivisibleSubset(In)
In=[4,8,10,240]
print a.largestDivisibleSubset(In)








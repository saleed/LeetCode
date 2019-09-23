class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()
        print(nums)
        pre=-float("inf")
        for i in range(len(nums)):
            if nums[i]==pre:
                continue
            pre=nums[i]
            cur=self.twosum(nums[i+1:],-nums[i])
            print(cur)
            for j in cur:
                new=[nums[i]]
                new.extend(j)
                res.append(new)
        return res

    def twosum(self,nums,target):
        if len(nums)<=1:
            return []
        res=[]
        p=0
        q=len(nums)-1
        while p<q:
            summ=nums[p]+nums[q]
            if target==summ:
                print(p,q)
                res.append([nums[p],nums[q]])
                while p+1<q and nums[p]==nums[p+1]:
                    p+=1
                p+=1
            elif summ<target:
                p+=1
                # res.append([nums[p],nums[q]])
            else:
                q-=1
        return res

a=Solution()
# nums= [-1, 0, 1, 2, -1, -4]
# print(a.threeSum(nums))
nums= [0,0,0,0]
print(a.threeSum(nums))


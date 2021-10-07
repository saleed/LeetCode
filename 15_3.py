class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        i=0
        res=[]
        while i <len(nums):
            curres=self.twoSum(nums,-nums[i],i+1,len(nums)-1)
            for v in curres:
                tmp=[nums[i]]
                tmp.extend(v)
                res.append(tmp)

            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            i+=1
        return res

    def twoSum(self,nums,target,p,q):
        res=[]
        while p<q:
            ###这里还可以用二分，速度更快
            if nums[p]+nums[q]==target:
                res.append([nums[p],nums[q]])
                while p<q and nums[p]==nums[p+1]:
                    p+=1
                p+=1
            elif nums[p]+nums[q]<target:
                p+=1
            else:
                q-=1
        return res

a=Solution()
nums = [-1,0,1,2,-1,-4]
print(a.threeSum(nums))
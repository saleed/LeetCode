class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.doublePtr(nums)



###超时
    def dfs(self,i,nums,target,tmp,tmpsum,res):
        if len(tmp)==3 and tmpsum<target:
            res.append(tmp[:])
            return
        if tmpsum<target and len(tmp)<3 and i<len(nums):
            self.dfs(i+1,nums,target,tmp,tmpsum,res)
            tmp.append(nums[i])
            self.dfs(i+1,nums,target,tmp,tmpsum+nums[i],res)
            tmp.pop()
##双指针
    def doublePtr(self,nums):
        nums.sort()
        cnt=0
        for i in range(len(nums)):
            p=i+1
            q=len(nums)-1
            while p<q:
                if nums[i]+nums[p]+nums[q]<target:
                    cnt+=(q-p)
                else:
                    p+=1
        return cnt






s=Solution()
nums = [-2,0,1,3]
target = 2
s.threeSumSmaller(nums,target)
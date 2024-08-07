####使用两个pre,处理数值重复

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        pre1=float("inf")
        res=[]
        for i in range(len(nums)-2):
            if nums[i]==pre1:
                continue
            pre1=nums[i]
            p=i+1
            q=len(nums)-1
            pre2=float("inf")
            while p<q:
                if pre2 == nums[p]:
                    p+=1
                    q-=1
                    continue
                pre2 = nums[p]
                if nums[p]+nums[q]==-nums[i]:
                    res.append([nums[i],nums[p],nums[q]])
                    p+=1
                    q-=1
                elif nums[p]+nums[q]<-nums[i]:
                    p+=1
                else:
                    q-=1

        return res







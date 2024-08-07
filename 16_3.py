class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        mindiff=float("inf")
        pre1=float("inf")
        minv=0
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i]==pre1:
                continue
            pre1=nums[i]
            p=i+1
            q=len(nums)-1
            # pre2=float("inf")
            print(nums)
            while p<q:
                if abs(nums[p]+nums[q]+nums[i]-target)<mindiff:
                    mindiff=abs(nums[p]+nums[q]+nums[i]-target)
                    minv=nums[p]+nums[q]+nums[i]
                    print(nums[i],nums[p],nums[q],minv,mindiff)

                if nums[p]+nums[q]+nums[i]==target:
                    return target
                elif nums[p]+nums[q]+nums[i]<target:
                    tmp=nums[p]
                    while p<q and nums[p]==tmp:
                        p+=1
                else:
                    tmp=nums[q]
                    while p<q and nums[q]==tmp:
                        q-=1
        return minv

nums =[4,0,5,-5,3,3,0,-4,-5]

target = -2
a=Solution()
print(a.threeSumClosest(nums,target))

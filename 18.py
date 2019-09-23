class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        prei=float("inf")

        res=[]
        for i in range(len(nums)):
            # print(nums[i], prei, nums[j], prej)
            if nums[i]==prei:
                continue
            prei=nums[i]
            prej = float("inf")
            for j in range(i+1,len(nums)):
                if prej==nums[j]:
                    continue
                # print(nums[i],prei,nums[j],prej)
                prej=nums[j]
                curtarget=target-nums[i]-nums[j]
                curres=self.twosum(nums[j+1:],curtarget)
                for ele in curres:
                    new=[nums[i],nums[j]]
                    new.extend(ele)
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
                # print(p,q)
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
nums = [1, 0, -1, 0, -2, 2]
print(a.fourSum(nums,0))

nums=[-7,-5,0,7,1,1,-10,-2,7,7,-2,-6,0,-10,-5,7,-8,5]


print(a.fourSum(nums,28))
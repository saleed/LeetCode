class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res=[]
        i=0
        nums.sort()
        while i<=len(nums)-3:
            # print(i)
            twosum=self.twosum(i+1,len(nums)-1,nums,-nums[i])

            for r in twosum:
                tmpres = [nums[i]]
                tmpres.extend(r)
                res.append(tmpres)

            while i+1<=len(nums)-3 and nums[i]==nums[i+1]:
                i+=1
            i+=1
        return res


    def twosum(self,i,j,nums,target):

        p=i
        q=j
        res=[]
        while p<q :
            if nums[p]+nums[q]==target:
                res.append([nums[p],nums[q]])
                while p+1<=q and nums[p]==nums[p+1]:
                    p+=1
                p+=1
            elif nums[p] + nums[q] < target:
                p+=1
            else:
                q-=1
            # print(p,q,res)
        return res
nums = [-1,0,1,2,-1,-4]
s=Solution()

print(s.threeSum(nums))
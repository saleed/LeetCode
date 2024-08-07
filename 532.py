class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """


        nums.sort()

        cnt=0
        if k==0:
            p=0
            while p<len(nums):
                pval=nums[p]
                pcnt=0
                while p<len(nums) and pval==nums[p]:
                    pcnt+=1
                    p+=1
                if pcnt>=2:
                    cnt+=1
            return cnt


        p=0
        q=1
        while q<len(nums):
            diff=nums[q]-nums[p]
            # print(p,q)
            if diff==k:
                cnt+=1
                pval=nums[p]
                while p<len(nums) and nums[p]!=pval:
                    p+=1
            elif diff<k:
                q+=1
            else:
                p+=1
        return cnt


ss=Solution()
tst=[1,3,1,5,4]
k=0
print(ss.findPairs(tst,k))
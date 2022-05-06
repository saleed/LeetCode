class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        presumdict={0:1}
        res=0
        presum=0

        for i in range(len(nums)):
            presum+=nums[i]
            if presum-k in presumdict:
                res+=presumdict[presum-k]

            if presum in presumdict:
                presumdict[presum]+=1
            else:
                presumdict[presum]=1


        return res
test=[0,0,0,0,0,0,0,0,0,0]
k=0
ss=Solution()
print(ss.subarraySum(test,k))

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        vdict={0:-1}
        pre=0
        maxl=0
        for i in range(len(nums)):
            if nums[i]==1:
                pre+=1
            else:
                pre-=1

            if pre in vdict:
                maxl=max(maxl,i-vdict[pre])
            else:
                vdict[pre]=i
            print(pre,vdict)

        return maxl


ss=Solution()
test=[0,0,1,0,0,0,1,1]
print(ss.findMaxLength(test))
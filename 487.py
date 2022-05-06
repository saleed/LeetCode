class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0

        preid=-1
        prelength=0##record the pre 1 list end id and length
        maxl=1
        i=0
        while i<len(nums):
            if nums[i]==0:
                i+=1
            else:
                p=i
                while i<len(nums) and nums[i]==1:
                    i+=1
                tmpl=i-p

                if preid==p-2:
                    maxl=max(maxl,tmpl+1+prelength)
                elif preid>0:
                    maxl=max(maxl,tmpl+1)
                else:
                    maxl=max(maxl,tmpl)
                preid=i-1
                prelength=tmpl
        if preid==len(nums)-2:
            maxl=max(maxl,prelength+1)
        return maxl









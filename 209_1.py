class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        i=0
        j=0
        max_seq=float("inf")
        tmpsum=0
        while True:
            if tmpsum>=target:
                print(j,i)
                max_seq=min(j-i,max_seq)
                if i<len(nums):
                    tmpsum-=nums[i]
                    i+=1
                else:
                    break
            else:
                if j<len(nums):
                    tmpsum+=nums[j]
                    j+=1
                else:
                    break
        if max_seq==float("inf"):
            return 0
        return max_seq
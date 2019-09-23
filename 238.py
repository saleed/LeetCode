class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tp=1
        zero=0
        for i in nums:
            if i==0:
                zero+=1
            else:
                tp*=i
        if zero>1:
            return [0]*len(nums)
        elif zero==1:
            res=[]
            for i in nums:
                if i!=0:
                    res.append(0)
                else:res.append(tp)
            return res
        else:
            res=[]
            for i in nums:
                res.append(tp/i)
            return res
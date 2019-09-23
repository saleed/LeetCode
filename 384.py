import random
class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums=nums
        self.pmt=self.getpmt(nums)


    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.__init__(self.nums)


    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        ret=self.pmt[random.randint(0,len(self.pmt)-1)]
        self.pmt.remove(ret)
        return ret
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

    def getpmt(self,nums):
        res=[]
        if len(nums)<=1:
            return [nums]
        for i in range(len(nums)):
            left=nums[:i]+nums[i+1:]
            # print left
            subres=self.getpmt(left)
            for ele in subres:
                new=[nums[i]]
                # print new
                new.extend(ele)
                # print new
                res.append(new)
        return res

nums=[1,2,3,4]
a=Solution(nums)
print a.getpmt(nums)


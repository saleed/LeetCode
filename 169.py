class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        buffer={}
        for i in nums:
            if len(buffer)==0:
                buffer[i]=1
            else:
                if i in buffer.keys():
                    buffer[i]+=1
                else:
                    buffer[list(buffer.keys())[0]]-=1
                    if buffer[list(buffer.keys())[0]]==0:
                        del buffer[list(buffer.keys())[0]]
        return list(buffer.keys())[0]


a={1:1,2:2,3:3}
print(a.keys())
print(list(a.keys())[0])

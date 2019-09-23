class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        pair=[]
        for i in range(len(nums)):
            pair.append([i,nums[i]])


        pair.sort(key=lambda i:i[1]) ###python里sort的用法
        p=0
        q=len(pair)-1
        while p<q:
            if pair[p][1]+pair[q][1]<target:
                p+=1
            elif pair[p][1]+pair[q][1]>target:
                q-=1
            else:
                return [pair[p][0],pair[q][0]]
        return [-1,-1]

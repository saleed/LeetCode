class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=0
        bestlen=float("inf")
        summ=0
        ###注意体会使用while循环以及使用for循环中索引的差异

        # for 循环中的索引其实是先移动指针后取值，
        # 下面写的是先操作后移动指针
        while right<len(nums) or (right==len(nums) and summ>=s): #中止条件
            if summ<s:
                summ+=nums[right]
                right+=1
            else: ##如果这里写else：上面的判别条件需要修改
                # if left==right:
                #     right+=1
                # summ-=nums[left]
                # left+=1
                while summ>=s:
                    bestlen=min(bestlen,right-left)
                    summ-=nums[left]
                    left+=1
        return bestlen





    def ptrthenOp(self,nums,s):
        if len(nums)==0:
            return 0
        left=-1
        right=-1
        bestlen=float("inf")
        summ=0
        while right<len(nums)-1: #中止条件
            if summ<s:
                right+=1
                summ+=nums[right]

            #####注意这里不能使用else 否则总会在上面的while判定条件出问题
            while summ>=s:
                bestlen=min(bestlen,right-left)
                left+=1
                summ-=nums[left]
        return bestlen if bestlen!=float("inf") else 0


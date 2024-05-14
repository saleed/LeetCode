class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()
        print(nums)
        ##增加使用set 内存翻倍 不适用set则需要多一层判断
        s=set()
        for i in range(len(nums)-2):
            p=i+1
            q=len(nums)-1
            target=-nums[i]
            while p<q:
                if nums[p]+nums[q]==target and (nums[i],nums[p],nums[q]) not in s:
                    res.append([nums[i],nums[p],nums[q]])
                    s.add((nums[i],nums[p],nums[q]))
                    p+=1
                elif nums[p]+nums[q]<target:
                    p+=1
                else:
                    q-=1
        return res




  def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()
        pre1=float("inf")
        pre2=float("inf")
        for i in range(len(nums)-2):
            p=i+1
            q=len(nums)-1
            target=-nums[i]
            if target==pre1:
                continue
            pre1=target
            while p<q:
                pre2
                if nums[p]+nums[q]==target:
                    res.append([nums[i],nums[p],nums[q]])
                    p+=1
                elif nums[p]+nums[q]<target:
                    p+=1
                else:
                    q-=1
        return res





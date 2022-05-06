# -*- coding:utf8 -*-


class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """


        for i in range(len(nums)):
            slow=i
            fast=(slow+nums[slow])%len(nums)
            flag=1 if nums[slow]>0 else -1
            k=0
            ##1.长度小于1,2.死循环，3.fast遇到反向

            print(i,slow,fast)
            while flag*nums[slow]>0 and flag*nums[fast]>0 and slow!=fast:
                print(slow,fast)
                slow=(slow+nums[slow])%len(nums)
                fast=(fast+nums[fast])%len(nums)
                # print(1,slow,fast)
                if flag*nums[fast]<0:
                    break
                fast=(fast+nums[fast])%len(nums)
                k+=1
                # print(k,fast,slow)
            if slow==fast and (slow+nums[slow])%len(nums)!=slow and k>1:
                return True

        return False
test=[3,1,2]
ss=Solution()
print(ss.circularArrayLoop(test))
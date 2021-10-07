class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        p=0
        q=len(nums)-1
        if nums[p]==target:
            return p
        if nums[q]==target:
            return q
        while p<=q: #小于等于也是个关键点
            mid=(p+q)/2
            print(mid,nums[mid])
            if nums[mid]==target:
                return mid
            if nums[p]<nums[mid]:
                if target<nums[mid] and target>=nums[p]:
                    ##注意这里一定是target>=nums[p]，因为更新的p和q有可能是从上一次的mid+1过来的，mid被检查过部位target 但是mid+1没有
                    q=mid

                else:
                    p=mid+1
                    #第二个要注意的点，p一定要更新为mid+1，因为当q=p+1的时候 mid会变成p，假如下次更新p=mid，会陷入死循环
            else:
                if target>nums[mid] and target<=nums[q]:
                    p=mid+1
                else:
                    q=mid

        return -1



if __name__=="__main__":
    a=Solution()
    nums=[4,5,6,7,0,1,2]
    target=0
    print(a.search(nums,target))



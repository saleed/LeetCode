class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ##使用分治算法
        return self.divideSolve(nums,0,len(nums)-1)




###分治算法仍然超时


    def divideSolve(self,nums,p,q):
        print(p,q)
        if p>q:
            return -float("inf")
        if p==q:
            return nums[p]
        if (q-p+1)%2==0:
            mid=(q-p+1)//2+p-1
            rightmax=-float("inf")
            leftmax=-float("inf")
            left=0
            right=0
            for j in range(mid+1,q+1):
                right+=nums[j]
                rightmax=max(rightmax,right)

            for j in range(mid+1)[::-1]:
                left+=nums[j]
                leftmax=max(leftmax,left)
            maxval=max(leftmax+rightmax,self.divideSolve(nums,p,mid),self.divideSolve(nums,mid+1,q)) #这里容易陷入死循环 mid=p
            return maxval
        else:
            mid = (q - p + 1)//2+p
            # rightmax = -float("inf")
            # leftmax = -float("inf")
            rightmax = 0
            leftmax = 0
            left = 0
            right = 0
            for j in range(mid + 1, q + 1):
                right += nums[j]
                rightmax = max(rightmax, right)

            for j in range(mid)[::-1]:
                left += nums[j]
                leftmax = max(leftmax, left)
            maxval = max(leftmax + rightmax +nums[mid], self.divideSolve(nums, p, mid-1), self.divideSolve(nums, mid + 1, q))
            return maxval


a=Solution()

test= [-2,1,-3,4,-1,2,1,-5,4]
test=[-2,1]
test=[1,2]
print(a.maxSubArray(test))



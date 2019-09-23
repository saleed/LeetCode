class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j=0
        nums.append(0)
        flag=0
        maxv=-float("inf")
        for i in range(len(nums)):
            if flag==0 and nums[i]!=0:
                flag=1
                j=i
            elif flag==1 and nums[i]==0:
                flag=0
                maxv=max(self.dp(nums[j:i]),maxv)
        for j in nums[:-1]:
            if j==0:
                return max(0,maxv)
        return maxv





    def dp(self,nums):
        if len(nums)==0:
            return
        if len(nums)==1 and nums[0]==0:
            return 0
        dp1=[1]*len(nums)
        dp2=[1]*len(nums)
        dp1[0]=nums[0]
        dp2[0]=nums[0]

        for t in range(1,len(nums)):
            if nums[t]>0:
                dp1[t]=max(nums[t],dp1[t-1]*nums[t])
                dp2[t]=min(nums[t],dp2[t-1]*nums[t])
            else:
                dp1[t]=max(nums[t],dp2[t-1]*nums[t])
                dp2[t]=min(nums[t],dp1[t-1]*nums[t])
        print(dp1)
        print(dp2)
        return max(dp1)


a=Solution()
test= [2,3,-2,4]
print(a.maxProduct(test))
test=[-2,0,-1]
print(a.maxProduct(test))
test=[3,-1,4]
print(a.maxProduct(test))



class Solution:
    def maxProduct(self, A):
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(max(A),max(B))



#注意这种方法！！！！
# class Solution {
#     public int maxProduct(int[] nums) {
#     int max = Integer.MIN_VALUE, imax = 1, imin = 1; // 一个保存最大的，一个保存最小的。
#     for (int i=0; i < nums.length; i++){
#         if (nums[i] < 0){int tmp = imax; imax = imin; imin = tmp;} // 如果数组的数是负数，那么会导致最大的变最小的，最小的变最大的。因此交换两个的值。
#             imax = Math.max(imax * nums[i], nums[i]);
#             imin = Math.min(imin * nums[i], nums[i]);
#
#     max = Math.max(max, imax);
# }


return max;
}
}
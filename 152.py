# class Solution(object):
#     def maxProduct(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if len(nums)==1:
#             return nums[0]
#
#         newnum=[]
#         mul=1
#         l=0
#         zero=0
#         while l<len(nums):
#             flag=0
#             while l<len(nums) and nums[l]>0:
#                 mul*=nums[l]
#                 l+=1
#                 flag=1
#             if flag:
#                 newnum.append(mul)
#                 mul=1
#             if l<len(nums):
#                 newnum.append(nums[l])
#                 l+=1
#         maxm=newnum[0]
#         print newnum
#         mul=1
#         for i in newnum:
#             if i==0:
#                 maxm = max(0,maxm)
#                 mul=1
#             else:
#                 mul*=i
#                 maxm=max(maxm,mul,i)
#         return maxm
# test=[3,-1,4]
# a=Solution()
# print a.maxProduct(test)

##wrong solution
#this question is very similar to subarray with maximum sum



#can not handle



####错误方法！！！！
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a= [0]*len(nums)
        a[0]=maxm=nums[0]
        for i in range(1,len(nums)):
            a[i]=max(nums[i],a[i-1]*nums[i])
            if a[i]>maxm:
                maxm=a[i]
        return maxm



a=Solution()
test= [2,3,-2,4]
print(a.maxProduct(test))
test=[-2,0,-1]
print(a.maxProduct(test))
test=[3,-1,4]
print(a.maxProduct(test))


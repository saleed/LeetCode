#思路
#方法1：使用集合 时间复杂度：O(n),空间复杂度O(n)
#方法2：排序后首位指针比较，时间复杂度为排序的复杂度，如果使用原地排序的方法，不需要额外空间，否则需要O(n)的空间复杂度

#方法2：
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


        pair.sort(key=lambda i:i[1])
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


# test slice

sl=Solution()
a=[1,2,3,5,6]

b=a[1:]
print(b) #python list slice


nums1=[2, 7, 11, 15]
nums2=[3,2,4]
print(sl.twoSum(nums1,9))
print(sl.twoSum(nums2,6))

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1=len(nums1)
        l2=len(nums2)
        k=int((l1+l2)/2)
        return self.recursiveSlove(nums1,nums2,l1,l2,k)

    def recursiveSlove(self,arr1,arr2,l1,l2,k):
        if l1==0:
            return arr2[k-1]
        if l2==0:
            return arr1[k-1]
        if l1+l2==k-1:
            return max(arr1[-1],arr2[-1])
        if int(l1/2)+int(l2/2)<k-1:
            return self.recursiveSlove(arr1[int(l1/2)+1:],arr2[int(l2/2)+1:],l1-int(l1/2),l2-int(l2/2),k-int(l1/2)-int(l2/2))
        if int(l1/2)+int(l2/2)>=k-1:
            return self.recursiveSlove(arr1[:int(l1/2)+1],arr2[:int(l2/2)+1],int(l1/2),int(l2/2),k)



a=[1,2]
b=[3,4]


test=Solution()
print(test.findMedianSortedArrays(a,b))
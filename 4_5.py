class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if (len(nums1)+len(nums2))%2==1:
            return self.findN(nums1,nums2,int(len(nums2)+len(nums1))/2+1)
        else:
            print("mid")
            l1=self.findN(nums1,nums2,int((len(nums2)+len(nums1))/2))
            print("###")
            l2=self.findN(nums1,nums2,int((len(nums2)+len(nums1))/2+1))
            # print(l1,l2)
            return (l1+l2)/2.0

    def findN(self,nums1,nums2,K): ##找序列中第K小的数字
        print(nums1,nums2,K)
        if len(nums1)==0:
            return nums2[K-1]
        if len(nums2)==0:
            return nums1[K-1]
        if K==1:
            return min(nums1[0],nums2[0])
        else:
            mid=int(K/2)-1
            # print(K,mid)
            mid=min(mid,len(nums1)-1,len(nums2)-1)########
            if nums1[mid]<nums2[mid]:
                return self.findN(nums1[mid+1:],nums2,int(K-(mid+1)))
            else:
                return self.findN(nums1,nums2[mid+1:],int(K-(mid+1)))




nums1 =[1]

nums2 =[2,3,4,5,6]

a=Solution()
print(a.findMedianSortedArrays(nums1,nums2))

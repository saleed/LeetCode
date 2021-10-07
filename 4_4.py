class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        p=0
        q=0

        if nums1==None and nums2==None:
            return -1
        tmp=pre=nums1[0]if len(nums1)>0 else nums2[0]
        sumlen=len(nums1)+len(nums2)
        cnt=sumlen/2

        while p<len(nums1) or q<len(nums2):

            pval=nums1[p] if p<len(nums1) else float("inf")
            qval=nums2[q] if q<len(nums2) else float("inf")
            pre=tmp
            if pval<qval:
                tmp=pval
                p+=1
            else:
                tmp=qval
                q+=1

            if p + q -1 == cnt:
                if sumlen % 2 == 0:
                    return (pre + tmp) / 2.0
                else:
                    return tmp





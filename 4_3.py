class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        find_index=set()
        total_len=len(nums2)+len(nums1)
        if total_len%2==0:
            find_index.add(total_len/2)
            find_index.add(total_len/2+1)
        else:
            find_index.add(total_len/2+1)


        p=0
        q=0
        sum_val=0.0
        while p<len(nums1) or q<len(nums2):
            tmp_val=float("inf")
            pval=float("inf")
            qval=float("inf")
            if p<len(nums1):
                pval=nums1[p]
            if q<len(nums2):
                qval=nums2[q]
            if pval<qval:
                tmp_val=nums1[p]
                p+=1
            else:
                tmp_val=nums2[q]
                q+=1
            if p+q in find_index:
                sum_val += float(tmp_val)

        return sum_val/len(find_index)


if __name__=="__main__":
    a=Solution()
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(a.findMedianSortedArrays(nums1,nums2))
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p=0
        q=0
        res=[]
        while p<m or q<n:
            pval=float("inf") if p==m else nums1[p]
            qval=float("inf") if q==n else nums2[q]
            if pval<qval:
                res.append(pval)
                p+=1
            else:
                res.append(qval)
                q+=1

        nums1= res
        return nums1
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
a=Solution()
print(a.merge(nums1,m,nums2,n))
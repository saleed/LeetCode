class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #binary search

        p=1
        q=len(nums)
        newnums=[-float("inf")]
        newnums.extend(nums)
        newnums.append(-float("inf"))
        while p<q:
            mid=int((p+q)/2)
            if newnums[mid]>newnums[mid+1] and newnums[mid]>newnums[mid-1]:
                return mid
            elif newnums[mid]<newnums[mid+1]:
                p=mid+1
            elif newnums[mid]<newnums[mid-1]:
                q=mid-1









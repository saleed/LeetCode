class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """


        candicate=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                candicate.append((nums1[i]+nums2[j],nums1[i],nums2[j]))


        candicate.sort(key=lambda x:x[0])
        print(candicate)
        res=[]
        for i in range(min(len(candicate),k)):
            res.append([candicate[i][1],candicate[i][2]])
        return res


s=Solution()
nums1=[1,7,11]
nums2=[2,4,6]
k=3
s.kSmallestPairs(nums1,nums2,k)
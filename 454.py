class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """


        ###hash

        adict={}
        bdict={}

        for i in nums1:
            for j in nums2:
                adict[i+j]=adict[i+j]+1 if i+j in adict else 0

        for i in nums3:
            for j in nums4:
                bdict[i+j]=bdict[i+j]+1 if i+j in bdict else 0
        res=0
        for k in adict:
            if -k in bdict:
                res+=adict[k]*bdict[-k]
        return res
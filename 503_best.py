class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        st=[]
        res=[-1]*len(nums)
        N=len(nums)
        for i in range(2*N):
            while len(st)>0 and nums[st[-1]]<nums[i%N]:
                res[st.pop()]=nums[i]
            st.append(i%N)
        # while len(st)>1:
        #     res[st.pop()]=nums[st[0]]
        # res[st[0]]=-1
        return res



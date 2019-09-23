class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i]==0:
                flag=0
                for j in range(i+1,len(nums)):
                    if nums[j]!=0:
                        nums[i],nums[j]=nums[j],nums[i]
                        flag=1
                        break
                if not flag:
                    break
        return nums
    def moveZeroes1(self,nums):
        st=[]
        for q in range(len(nums)):
            if nums[q]==0:
                st.append(q)
            else:
                if len(st)>0:
                    nums[st[0]]=nums[q]
                    nums[q]=0
                    st.append(q)
                    st=st[1:]
        print nums

a=Solution()

test1=[0, 1, 0, 3, 12]

print a.moveZeroes1(test1)
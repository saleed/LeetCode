class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """


        ##问题转换为，给定两个数啊a 和b , 每次选择一个大于0的起点按照间隔b 叠加至a，则要选择多个个起点才能遍历全a点之前的所有记录
        ##答案为ab的最小公约数
        k=k%len(nums)
        cnt=0
        for i in range(0,k):
            n=1
            tmp=nums[i]
            print(nums)
            while (i+n*k)%len(nums)!=i:
                newtmp=nums[(i+n*k)%len(nums)]
                nums[(i+n*k)%len(nums)]=tmp
                tmp=newtmp
                n+=1
                cnt+=1
            

            nums[i]=tmp
            if cnt == len(nums):
                return



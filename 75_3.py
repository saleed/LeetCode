class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p=0
        q=len(nums)-1

        i=0
        while i<=q:
            if i>q:
                break
            else:
                if nums[i]==0:
                    nums[i],nums[p]=nums[p],nums[i]
                    p+=1
                    if i<p:
                        i+=1
                elif nums[i]==2:
                    nums[i],nums[q]=nums[q],nums[i]
                    q-=1
                else:
                    i+=1
        # print(nums)



#这道题可以有两种解法：
#1.两次遍历 第一次更新头部0，第二次更新尾部为2 快速排序的方法，根据一个标准，选择一个位置左边的满足某个标准，右边不满足这个标准
#2.一次遍历，头尾两个指针，

a=Solution()
color= [2,0,2,1,1,0]
print(a.sortColors(color))

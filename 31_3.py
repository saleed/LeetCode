#想到了一个普通思路，首先，如果任意交换两个数a b,a下标小于b,如果a<b,交换过后的数一定比原来的数大
#所以可以遍历符合a<b的 a b其中最小的那个即满足条件的那个，复杂度为O(n2)



#再深一层考虑，在遍历过程中，给定一个确定的b,a必然是离尾部越近越好，这样可以减少搜索的步数，




# 反过来，给定一个a 能够使交换后的数刚好大于原先的数，那么这个b必然是a后面大于a但又最接近a的数，而且a肯定是离尾部越近越好

#综上考虑，即得出了一个标准的算法






class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        id=0

        for i in range(1,len(nums))[::-1]:
            if nums[i]<=nums[i-1]:
                continue
            else:
                print(i)
                id=i
                for j in range(i,len(nums))[::-1]:
                    if nums[j]>nums[i-1]:
                        nums[j],nums[i-1]=nums[i-1],nums[j]
                        # print(i-1,j)
                        break
                break
        p=id
        q=len(nums)-1
        while p<q:
            nums[p],nums[q]=nums[q],nums[p]
            p+=1
            q-=1
        return nums






a=Solution()
print(a.nextPermutation([1,3,2]))
# print(range(5))
print(a.nextPermutation([3,2,1]))

print(a.nextPermutation([1,2,3]))
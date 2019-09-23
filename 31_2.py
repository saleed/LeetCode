class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #
        # 判断按照字典序有木有下一个，如果完全降序就没有下一个
        # 如何判断有木有下一个呢？只要存在a[i - 1] < a[i]
        # 的升序结构，就有，而且我们应该从右往左找，一旦找到，因为这样才是真正下一个
        # 当发现a[i - 1] < a[i]
        # 的结构时，从在[i, ∞]中找到最接近a[i - 1]
        # 并且又大于a[i - 1]
        # 的数字，由于降序，从右往左遍历即可得到k
        # 然后交换a[i - 1]
        # 与a[k]，然后对[i, ∞]排序即可，排序只需要首尾不停交换即可，因为已经是降序
        # 上面说的很抽象，还是需要拿一些例子思考才行，比如[0, 5, 4, 3, 2, 1]，下一个是[1, 0, 2, 3, 4, 5]

        i=len(nums)-1
        while i>0 and nums[i]<=nums[i-1]:
            i-=1
        if i!=0:
            for j in list(reversed(range(i,len(nums)))):
                if nums[j]>nums[i-1]:
                    nums[j],nums[i-1]=nums[i-1],nums[j]
                    break
        p=i
        q=len(nums)-1
        while p<q:
            nums[p],nums[q]=nums[q],nums[p]
            p+=1
            q-=1
        return nums




a=Solution()
print(a.nextPermutation([1,3,2]))
# print(range(5))
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = self.nonRecursive(nums)
        return res


    def recursive(self, nums, i, res):
        if i >= len(nums):
            res.append(nums[:])
            return
        self.recursive(nums, i + 1, res)
        for v in range(i + 1, len(nums)):
            # if nums[v] == nums[i]: ###这种写法是错误的  要判断num[i]是否都访问过
            #     continue

            if nums[j] in nums[i:j]:
                continue
            nums[v], nums[i] = nums[i], nums[v]
            self.recursive(nums, i + 1, res)
            nums[i], nums[v] = nums[v], nums[i]


    def nonRecursive(self, nums):
        res = []
        nums.sort()
        while True:
            res.append(nums[:])
            p = len(nums) - 1
            while p > 0 and nums[p] <= nums[p - 1]: ## < change to <=
                p -= 1

            if p == 0:
                break
            print("0",nums)
            q = len(nums) - 1
            swap = p - 1
            while q > swap and nums[q] <= nums[swap]: ##< change to <=
                q -= 1
            nums[q], nums[swap] = nums[swap], nums[q]
            print("1",nums)
            q = len(nums) - 1
            while p < q:
                nums[p], nums[q] = nums[q], nums[p]
                p += 1
                q -= 1

            print("2",nums)
        return res

#
# test = [1,1,2]
# a=Solution()
# print(a.permuteUnique(test))

test=[1,11,1,111,2]
print(test[1:1])


test=[[1,2,3,4],[5,6,7,8]]
print(test[1:2][2:])


d={}
for i in range(5):
    d[i]=[i]
print(d.values())
print(list("234"))
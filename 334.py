class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """


        # 找到最小和次小，只要有一个数大于次小，则必然有递增三元子序列
        # 次小总是再最小后更新，因此能保证次小必然在最小的后面
        c1=float("inf")
        c2=float("inf")
        for i in nums:
            if i<=c1:
                c1=i
            elif i<=c2:
                c2=i
            else:
                return True
        return False


    #if we remove the limit of length 3,and change the question to get the max length of increaing path
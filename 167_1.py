class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        p=0
        q=len(numbers)-1
        while p<q:
            if numbers[p]+numbers[q]==target:
                return [p+1,q+1]
            elif numbers[p]+numbers[q]<target:
                p+=1
            else:
                q-=1
        return
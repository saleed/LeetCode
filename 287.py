class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """



        #use hash table: (O(n) time and O(n) space
        return (sum(nums)-sum(list(set(nums))))/(len(nums)-len(list(set(nums))))
        #use sort:(O(n) time O(1) space)

        #use binary search


        ##O(n) space and O(1) time floyd-algorithm to find cycle  VERY IMPORTANT!!!!!!
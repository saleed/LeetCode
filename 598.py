class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """

        minw=float("inf")
        minh=float("inf")
        for i in range(len(ops)):
            minw=min(ops[0],minw)
            minh=min(ops[1],minh)
        return minw*minh

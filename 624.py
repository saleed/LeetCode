class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """

        maxdiff = -float("inf")
        tmp = [arrays[0][0], arrays[0][-1]]
        for v in arrays[1:]:
            if (v[0] >= tmp[0] and v[-1] <= tmp[1]) or   (v[0]<= tmp[0] and v[-1] >= tmp[1]) :
                maxdiff = max(maxdiff, tmp[1] - v[0], v[-1] - tmp[0])
            else:
                # print(tmp[1],v[-1])
                maxdiff = max(tmp[1], v[-1]) - min(tmp[0], v[0])
                tmp = [min(tmp[0], v[0]), max(tmp[1], v[-1])]
        return maxdiff

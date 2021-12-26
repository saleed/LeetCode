class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """

        areaa=(ay2-ay1)*(ax2-ax1)
        areab=(by2-by1)*(bx2-bx1)
        leftx=max(ax1,bx1)
        rightx=min(ax2,bx2)

        boty=max(ay1,by1)
        upy=min(ay2,by2)

        if leftx>rightx or upy<boty:
            return areaa+areab
        return areaa+areab- (rightx-leftx)*(upy-boty)



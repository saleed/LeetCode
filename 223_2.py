class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        if C<=E or G<=A or D<=F or H<=B:
            return abs((D-B)*(C-A))+abs((H-F)*(G-E))
        return abs((D-B)*(C-A))+abs((H-F)*(G-E))-abs((min(C,G)-max(A,E))*(min(D,H)-max(B,F)))



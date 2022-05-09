class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """


        if r*c!=len(mat)*len(mat[0]):
            return mat


        res=[[0 for _ in range(c)] for _ in range(r)]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                ni=(i*len(mat[0])+j)/c
                nj=(i*len(mat[0])+j)%c
                res[ni][nj]=mat[i][j]
        return res




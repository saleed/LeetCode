import copy as cp
b = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]



class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.life(board,1)



    def life(self,b, gen):

        for t in range(gen):
            new_b = cp.deepcopy(b)
            for i in range(len(new_b)):
                for j in range(len(new_b[0])):
                    dot, dot1 = 0, 0
                    for x, y in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                                 (i + 1, j - 1), (i + 1, j), (i + 1, j + 1),
                                 (i, j - 1), (i, j + 1)]:
                        if 0 <= x < len(new_b) and 0 <= y < len(new_b[0]):
                            # if 0 <= x < len(new_b) and 0 <= y < len(new_b[0]) and\
                            #     new_b[x][y] == 1:
                            if new_b[x][y] == 0:
                                dot += 1
                            else:
                                dot1 += 1

                    b[i][j] = 1 if (dot1 in (2, 3) and b[i][j] == 1) or \
                                   (dot1 == 3 and b[i][j] == 0) else 0

                    # b[i][j] = (1 if dot1 in (2, 3) or dot == 3 else 0)
                    # life(b, 1)
                    # Out[158]:
                    # [[1, 0, 0, 0, 0, 1],
                    #  [0, 0, 0, 0, 0, 0],
                    #  [0, 0, 0, 0, 0, 0],
                    #  [0, 0, 0, 0, 0, 0],
                    #  [0, 0, 0, 0, 0, 0],
                    #  [1, 0, 0, 0, 0, 1]]

                    # if b_old[r][c]==1:
                    #     if (sum(result)==2)|(sum(result)==3):
                    #         b_new[r][c]=1
                    #     else:
                    #         b_new[r][c]=0
                    # else:
                    #     if sum(result)==3:
                    #         b_new[r][c]=1
                    #     else:
                    #         b_new[r][c]=0

                    # if new_b[i][j] == 1:

        return b

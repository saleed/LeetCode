# coding=UTF-8


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """



    def solve1(self,matrix):

        vis = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        n = 0
        x = 0
        y = -1
        res = []
        while n < len(matrix) * len(matrix[0]):
            while y + 1 < len(matrix[0]) and vis[x][y + 1] == 0:
                y += 1
                res.append(matrix[x][y])
                vis[x][y] = 1
                n += 1
            while x + 1 < len(matrix) and vis[x + 1][y] == 0:
                x += 1
                res.append(matrix[x][y])
                vis[x][y] = 1
                n += 1
            while y - 1 < len(matrix[0]) and vis[x][y - 1] == 0:
                y -= 1
                res.append(matrix[x][y])
                vis[x][y] = 1
                n += 1
            while x - 1 < len(matrix) and vis[x - 1][y] == 0:
                x -= 1
                res.append(matrix[x][y])
                vis[x][y] = 1
                n += 1

        return res

    #
    # def solve2(self,matrix):
    #     m=len(matrix)
    #     n=len(matrix[0])
    #     for n in range(min(m,n)/2):




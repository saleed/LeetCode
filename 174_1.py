class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        aggmax = [[0 for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]
        pathminmax = [[0 for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]

        for i in range(len(dungeon)):
            for j in range(len(dungeon[0])):
                if i == 0 and j == 0:
                    aggmax[0][0] = dungeon[0][0]
                    pathminmax[0][0] = dungeon[0][0]
                elif i == 0:
                    aggmax[i][j] = aggmax[i][j - 1] + dungeon[i][j]
                    pathminmax[i][j] = min(pathminmax[i][j - 1], aggmax[i][j - 1] + dungeon[i][j])
                elif j == 0:
                    aggmax[i][j] = aggmax[i - 1][j] + dungeon[i][j]
                    pathminmax[i][j] = min(pathminmax[i - 1][j], aggmax[i - 1][j] + dungeon[i][j])
                else:
                    aggmax[i][j] = max(aggmax[i - 1][j], aggmax[i][j - 1]) + dungeon[i][j]
                    pathminmax[i][j] = max(min(pathminmax[i - 1][j], aggmax[i - 1][j] + dungeon[i][j]),
                                           min(pathminmax[i][j - 1], aggmax[i][j - 1] + dungeon[i][j]))
        for i in range(len(dungeon)):
            print(aggmax[i])

        for i in range(len(dungeon)):
            print(pathminmax[i])
        return abs(min(pathminmax[-1][-1], 0)) + 1



a=Solution()
test=[[1,-4,5,-99],
      [2,-2,-2,-1]]
print(a.calculateMinimumHP(test))
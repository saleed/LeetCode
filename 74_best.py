class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

###脑子里应该想着阴影范围，任何一个位置，右下角区域比当前位置大，左上角比当前位置小，其余位置无法判断
###
        row=-1
        while row+1<len(matrix) and target>matrix[row+1][0]:
            row+=1
        print(row)

        for i in range(len(matrix[0])):
            if target==matrix[row][i]:
                return True

        return False


target=3
mt=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
a=Solution()
print(a.searchMatrix(mt,target))
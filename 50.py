class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        self.swapLine(matrix)





    def swapLine(self,matrix):
        for i in range(len(matrix)/2):
            for j in range(i,len(matrix[0])-i-1):#注意这里一定是len(matrix[0])-i-1 ,否则会出现一个边角的点呗替换两次
                cord1=[j,len(matrix[0])-i-1]
                cord2=[len(matrix)-i-1,len(matrix[0])-j-1]
                cord3=[len(matrix)-j-1,i]
                matrix[i][j], matrix[cord1[0]][cord1[1]], matrix[cord2[0]][cord2[1]], matrix[cord3[0]][cord3[1]] = \
                matrix[cord3[0]][cord3[1]],matrix[i][j],matrix[cord1[0]][cord1[1]], matrix[cord2[0]][cord2[1]]

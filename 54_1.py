class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        count=0
        row=0
        col=-1
        res=[]
        vis=[[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        while count<len(matrix)*len(matrix[0]):
            ##使用col+1去试探下一个位置是否合法，此时必须初始化初始位置为[0,-1]!!
            while col+1<len(matrix[0]) and vis[row][col+1]==0:
                col+=1
                res.append(matrix[row][col])
                vis[row][col]=1
                count+=1
            while row+1<len(matrix) and vis[row+1][col]==0:
                row+=1
                res.append(matrix[row][col])
                vis[row][col]=1
                count+=1
            while col-1>=0 and vis[row][col-1]==0:
                col-=1
                res.append(matrix[row][col])
                vis[row][col] = 1
                count+=1
            while row-1>=0 and vis[row-1][col]==0:
                row-=1
                res.append(matrix[row][col])
                vis[row][col]=1
                count+=1
        return res






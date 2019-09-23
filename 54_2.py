class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix)==0:
            return []
        if len(matrix[0])==0:
            return []
        m=len(matrix)
        n=len(matrix[0])

        count=1
        res=[matrix[0][0]]
        row=0
        col=0
        vis=[[0 for i in range(len(matrix[0]))] for _ in range(len(matrix))]
        vis[0][0]=1
        while count<m*n:
            while col+1<n and vis[row][col+1]==0:
                col+=1
                res.append(matrix[row][col])
                vis[row][col]=1
                count+=1
            while row+1<m and vis[row+1][col]==0:
                row+=1
                vis[row][col]=1
                res.append(matrix[row][col])
                count+=1
            while col-1>=0 and vis[row][col-1]==0:
                col-=1
                res.append(matrix[row][col])
                vis[row][col]=1
                count+=1
            while row-1>=0 and vis[row-1][col]==0:
                row-=1
                res.append(matrix[row][col])
                vis[row][col]=1
                count+=1
        return res




mat=[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
a=Solution()
print(a.spiralOrder(mat))

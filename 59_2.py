class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        count=1
        # res=[matrix[0][0]]
        row=0
        col=0
        vis=[[0 for i in range(n)] for _ in range(n)]
        matrix = [[0 for i in range(n)] for _ in range(n)]
        matrix[0][0]=1
        vis[0][0]=1
        while count<n*n:
            while col+1<n and vis[row][col+1]==0:
                col+=1
                count+=1
                matrix[row][col]=count
                vis[row][col]=1
            while row+1<n and vis[row+1][col]==0:
                row+=1
                count+=1
                matrix[row][col] = count
                vis[row][col]=1

            while col-1>=0 and vis[row][col-1]==0:
                col-=1
                count+=1
                matrix[row][col] = count
                vis[row][col]=1

            while row-1>=0 and vis[row-1][col]==0:
                row-=1
                count+=1
                matrix[row][col] = count
                vis[row][col]=1

        return matrix




n=3
a=Solution()
print(a.generateMatrix(3))

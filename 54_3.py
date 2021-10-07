# coding=UTF-8


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """


        vis=[[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        x=0
        y=-1
        cnt=0
        res=[]
        ##尝试下一个点的位置
        while cnt<len(matrix)*len(matrix[0]):
            print(cnt)
            while y+1<len(matrix[0]) and vis[x][y+1]==0:
                cnt+=1
                y+=1
                vis[x][y]=1
                res.append(matrix[x][y])
            while x+1<len(matrix) and vis[x+1][y]==0:
                cnt+=1
                x+=1
                vis[x][y]=1
                res.append(matrix[x][y])
            while y-1>=0 and vis[x][y-1]==0:
                cnt+=1
                y-=1
                vis[x][y]=1
                res.append(matrix[x][y])
            while x-1>=0 and vis[x-1][y]==0:
                cnt+=1
                x-=1
                vis[x][y]=1
                res.append(matrix[x][y])
        return res




mat=[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
a=Solution()
print(a.spiralOrder(mat))

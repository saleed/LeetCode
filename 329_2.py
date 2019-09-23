class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix)==0 or len(matrix[0])==0:
            return 0
        maxlen=-float("inf")
        vis=[[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # print("####")
                vis[i][j]=1
                maxlen=max(maxlen,self.dfs(vis,matrix,1,matrix[i][j],i,j))
                vis[i][j]=0
        return maxlen




    def dfs(self,vis,matrix,curlen,pre,x,y):
        # print(x,y,pre,curlen)
        dx=[1,0,-1,0]
        dy=[0,1,0,-1]
        maxlen=curlen
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=len(matrix) or ny<0 or ny>=len(matrix[0]):
                continue
            if vis[nx][ny]==1 or matrix[nx][ny]<=pre:
                continue
            vis[nx][ny]=1
            # 变量不能重用
            # pre=matrix[nx][ny]
            # maxlen=max(maxlen,self.dfs(vis,matrix,curlen+1,pre,nx,ny))
            newpre=matrix[nx][ny]
            maxlen=max(maxlen,self.dfs(vis,matrix,curlen+1,newpre,nx,ny))
            vis[nx][ny]=0
        return maxlen



a=Solution()
nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]

print(a.longestIncreasingPath(nums))


nums=[
    [3,4,5],
    [3,2,6],
    [2,2,1]]
print(a.longestIncreasingPath(nums))

nums=[[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]
print(a.longestIncreasingPath(nums))

class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        vis=set()
        cnt=0
        for i in range(len(isConnected)):
            if i not in vis:

                self.dfs(vis,i,isConnected)
                cnt+=1
                print(vis,cnt)
        return cnt



    def dfs(self,vis,i,isConnected):
        if i in vis:
            return
        vis.add(i)
        for j in range(len(isConnected)):
            if isConnected[i][j]==1 and j not in vis:
                self.dfs(vis,j,isConnected)
test=[[1,1,0],[1,1,0],[0,0,1]]

ss=Solution()
print(ss.findCircleNum(test))
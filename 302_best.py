class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """

        left=float("inf")
        right=-float("inf")
        up=-float("inf")
        down=float("inf")

        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j]=="1":
                    left = min(left, i)
                    right = max(right, i)
                    up = max(up, j)
                    down = min(down, j)
                    # left,right,down,up=self.bfs(i,j,image)
                    # return (right-left+1)*(up-down+1)

        return (right-left+1)*(up-down+1)


    def bfs(self,x,y,image):
        que=[[x,y]]

        left=float("inf")
        right=-float("inf")
        up=-float("inf")
        down=float("inf")

        vis=set()
        dx=[1,0,-1,0]
        dy=[0,1,0,-1]
        while len(que)>0:
            head=que[0]
            tmpx=head[0]
            tmpy=head[1]
            vis.add(tmpx*len(image[0])+tmpy)
            que=que[1:]

            for i in range(4):
                nx=tmpx+dx[i]
                ny=tmpy+dy[i]
                if 0<=nx<len(image) and 0<=ny<len(image[0]) and nx*len(image[0])+ny not in vis and image[nx][ny]=="1":
                    que.append([nx,ny])

        return left,right,down,up


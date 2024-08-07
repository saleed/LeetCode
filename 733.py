class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        que=[(sr,sc)]
        vis=set()
        vis.add((sr,sc))
        dx=[1,0,-1,0]
        dy=[0,1,0,-1]
        src_color=image[sr][sc]
        while len(que)>0:
            head=que[0]
            print(head)
            que=que[1:]
            x=head[0]
            y=head[1]
            image[x][y]=color
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if nx>=0 and ny>=0 and nx<len(image) and ny<len(image[0]) \
                        and image[nx][ny]==src_color and (nx,ny) not in vis:
                    que.append((nx,ny))
                    vis.add((nx,ny))
        return image






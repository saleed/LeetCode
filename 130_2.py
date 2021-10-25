class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        vis=set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                pos=i*len(board[0])+j

                if  pos in vis or board[i][j]=='X':
                    continue
                else:
                    print("##",i,j)
                    self.bfs(pos,vis,board)

    def bfs(self,pos,vis,board):
        dx=[0,1,0,-1]
        dy=[1,0,-1,0]
        queue=[pos]
        flag=0
        res=[]
        while len(queue)>0:

            head=queue[0]
            print(head)
            queue=queue[1:]
            x = head / len(board[0])
            y = head % len(board[0])
            res.append(head)
            if  x== 0 or y == 0 or x == len(board) - 1 or y == len(board[0]) - 1:
                flag = 1
            for i in range(4):
                newx=x+dx[i]
                newy=y+dy[i]
                newpos=newx*len(board[0])+newy
                if 0 <= newx < len(board) and 0 <= newy < len(board[0]) and newpos not in vis and board[newx][newy]=='O':
                    queue.append(newpos)
                    vis.add(newpos)  ###如果访问记录写到for之前会产生很严重的后果。。。。。


        print("flag",flag,"res",res)
        if flag==0:
            for p in res:
                board[p/len(board[0])][p%len(board[0])]='X'


test=[["X","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"],["O","X","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O","X","X"],["O","O","O","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","X"],["O","O","X","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","X","O"],["O","O","O","O","O","X","O","O","O","O","X","O","O","O","O","O","X","O","O","X"],["X","O","O","O","X","O","O","O","O","O","X","O","X","O","X","O","X","O","X","O"],["O","O","O","O","X","O","O","X","O","O","O","O","O","X","O","O","X","O","O","O"],["X","O","O","O","X","X","X","O","X","O","O","O","O","X","X","O","X","O","O","O"],["O","O","O","O","O","X","X","X","X","O","O","O","O","X","O","O","X","O","O","O"],["X","O","O","O","O","X","O","O","O","O","O","O","X","X","O","O","X","O","O","X"],["O","O","O","O","O","O","O","O","O","O","X","O","O","X","O","O","O","X","O","X"],["O","O","O","O","X","O","X","O","O","X","X","O","O","O","O","O","X","O","O","O"],["X","X","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O","O"],["O","X","O","X","O","O","O","X","O","X","O","O","O","X","O","X","O","X","O","O"],["O","O","X","O","O","O","O","O","O","O","X","O","O","O","O","O","X","O","X","O"],["X","X","O","O","O","O","O","O","O","O","X","O","X","X","O","O","O","X","O","O"],["O","O","X","O","O","O","O","O","O","O","X","O","O","X","O","X","O","X","O","O"],["O","O","O","X","O","O","O","O","O","X","X","X","O","O","X","O","O","O","X","O"],["O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"],["X","O","O","O","O","X","O","O","O","X","X","O","O","X","O","X","O","X","O","O"]]
a=Solution()
print(a.solve(test))
for v in test:
    print(v)
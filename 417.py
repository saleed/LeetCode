import queue
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix)==0 or len(matrix[0])==0:
            return []
        cord=[[matrix[m][n],complex(m,n)] for n in range(len(matrix[0])) for m in range(len(matrix))]
        cord=sorted(cord,key=lambda x:x[0])
        # print(cord)

        toPacific=[[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        toAlantic = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]


        dx=[1,0,-1,0]
        dy=[0,1,0,-1]


        for i in range(len(matrix)):
            toPacific[i][0]=True
            toAlantic[i][len(matrix[0])-1]=True
        for j in range(len(matrix[0])):
            toPacific[0][j]=True
            toAlantic[len(matrix)-1][j]=True

        for pair in cord:
            x = int(pair[1].real)
            y = int(pair[1].imag)
            for i in range(4):
                nx=int(x+dx[i])
                ny=int(y+dy[i])
                if nx>=0 and nx<len(matrix) and ny>=0 and ny<len(matrix[0]):
                    if toPacific[nx][ny]==True and matrix[nx][ny]<=matrix[x][y]:
                        toPacific[x][y]=True

        for pair in cord:
            x = int(pair[1].real)
            y = int(pair[1].imag)
            for i in range(4):
                nx = int(x + dx[i])
                ny = int(y + dy[i])
                if nx >= 0 and nx < len(matrix) and ny >= 0 and ny < len(matrix[0]):
                    if toAlantic[nx][ny] == True and matrix[nx][ny] <= matrix[x][y]:
                        toAlantic[x][y] = True

        # print(toPacific)
        # print(toAlantic)



        res=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if toAlantic[i][j] and toPacific[i][j]:
                    res.append([i,j])
        return res


    def genSetArr(self,mt):
        if len(mt)==0 or len(mt[0])==0:
            return []





    def bfs(self,mt,state,x,y):
        res=set()
        que=queue.Queue()
        que.put(complex(x,y))
        state[x][y]=1
        dx=[1,0,-1,0]
        dy=[0,1,0,-1]
        while not que.empty():
            tmp=que.get()
            for i in range(4):
                nx=tmp.real()+dx[i]
                ny=tmp.imag()+dy[i]
                if nx >= 0 and nx < len(mt) and ny >= 0 and ny < len(mt[0]) and state[nx][ny]==0 and tmp[nx][ny]:

a=Solution()


m=[[1,2,2,3,5],
   [3,2,3,4,4],
   [2,4,5,3,1],
   [6,7,1,4,5],
   [5,1,1,2,4]]
print(a.pacificAtlantic(m))



#未过用例，当矩阵种含有相邻的相同值时候
m=[[10,10,10],[10,1,10],[10,10,10]]
print(a.pacificAtlantic(m))




def TestComplex():

    print(1+2j)
    m=1
    n=2
    c=complex(m,n)



    print(c)

TestComplex()



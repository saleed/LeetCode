import Queue

def exist(self, board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """

    q = Queue.Queue()
    q.put()


dx=[1,0,-1,0]
dy=[0,1,0,-1]


class node:
    def __init__(self,x,y,val):
        self.x=x
        self.y=y
        self.val=val
        self.candidate=[0]*4


def dfs(st,mtx,target,cur):
    if cur==target:
        return True
    nd=st[len(st)-1]
    for i in range(4):
        if nd.candidate[i]==0 and isInArea(nd.x,nd.y,mtx,i) and mtx[nd.x+dx[i]][nd.y+dy[i]]==0 and :
            mtx[nd.x + dx[i]][nd.y + dy[i]]=1
            nd.candidate[i]=1
            newnode=node(nd.x + dx[i],nd.y+dy[i],mtx,target,)






def isInArea(x,y,mtx,i):
    if x + dx[i] < len(mtx[0]) and y + dy[i]<len(mtx) and x + dx[i] >=0 and y+dy[i]>=0:
        return True
    return False


a=[[1],2,3,4,5]
b=a[0]
b[0]=2
print a




 ,







def quickSort(nums,p,q):
    id=partition(nums,p,q)
    if id==-1:
        return
    quickSort(nums,p,id-1)
    quickSort(nums,id+1,q)


def partition(nums,p,q):
    if p>=q:
        return -1
    id=0
    for i in range(p,q+1):
        if nums[i]<nums[id]:
            nums[i],nums[id]=nums[id],nums[i]
            id+=1
    nums[q],nums[id]=nums[id],nums[q]
    return id


test=[2,1,6,8,3,9,0]
quickSort(test,0,len(test)-1)
print(test)



def printCircle(n):

    x=0
    y=-1

    i=0
    res=[[0 for _ in range(n)] for _ in range(n)]
    vis=[[0 for _ in range(n)] for _ in range(n)]
    while i<n*n:
        while y+1<n and vis[x][y+1]==0:
            y+=1
            res[x][y]=i+1
            vis[x][y]=1
            i+=1
        while x+1<n and vis[x+1][y]==0:
            x+=1
            res[x][y]=i+1
            vis[x][y]=1
            i+=1
        while x - 1>=0 and vis[x-1][y]==0:
            x -= 1
            res[x][y] = i + 1
            vis[x][y] = 1
            i += 1
        while y - 1>=0and vis[x][y-1]==0:
            y -= 1
            res[x][y] = i + 1
            vis[x][y] = 1
            i += 1


    return res

print(printCircle(3))



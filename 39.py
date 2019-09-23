import  copy
def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]

    """
    rlt=[]
    left=target
    find(0,left,candidates,[],rlt)
    print rlt


def find(i,left,candi,cur,rlt):
    # print i,left,cur
    if left==0:
        rlt.append(cur)
        return
    if i==len(candi) or left<0:
        return
    find(i+1,left,candi,cur,rlt)
    j=1
    while left-j*candi[i]>=0:
        newcur = copy.deepcopy(cur)
        for t in range(j):
            newcur.append(candi[i])
        # print newcur
        find(i + 1, left - j*candi[i], candi,newcur, rlt)
        j=j+1
    return


test=[2,3,6,7]

combinationSum(test,7)






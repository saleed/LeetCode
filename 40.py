import copy
def combinationSum2(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """

    rlt=[]
    left=target
    nums,newcandi=preporcess(candidates)
    find(0,left,nums,newcandi,[],rlt)
    print rlt


def find(i,left,nums,candi,cur,rlt):
    # print i,left,cur
    if left==0:
        rlt.append(cur)
        return
    if i>=len(candi) or left<0:
        return
    find(i+1,left,nums,candi,cur,rlt)
    j=1
    while j<=nums[i]:
        newcur = copy.deepcopy(cur)
        for t in range(j):
            newcur.append(candi[i])
        find(i + 1, left - j*candi[i],nums, candi,newcur, rlt)
        j=j+1
    return


def preporcess(candi):
    candi.sort()
    print candi
    nums=[]
    pre=-1
    start=-1
    num=1
    newcandi=[]
    for i in candi:
        if i==pre:
            nums[-1]=nums[-1]+1
        else:
            newcandi.append(i)
            nums.append(1)
            pre=i
    return nums,newcandi


test=[10,1,2,7,6,1,5]
print preporcess(test)
print combinationSum2(test,8)


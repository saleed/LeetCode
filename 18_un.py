import copy


def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    nums.sort()
    cursel=[]
    rlt=[]
    sum(nums,target,cursel,0,rlt)
    print rlt





def sum(nums,target,cursel,sumsel,result):
    print cursel,sumsel,nums
    if sumsel>target:
        return
    if len(cursel)==4:
        if sumsel!=target:
            return
        else:
            result.append(cursel)
            return
    if len(nums) == 0:
        return
    for i in range(len(nums)):
        newnums=rmvOne(nums,i)
        newsel=copy.deepcopy(cursel)
        newsel.append(nums[i])
        newsum=sumsel+nums[i]
        sum(newnums,target,newsel,newsum,result)
    return





def rmvOne(nums,i):
    d=[]
    for j in range(len(nums)):
        if j==i:
            continue
        d.append(nums[j])
    return d




#
# nums = [1, 0, -1, 0, -2, 2]
# target = 0
#
# print fourSum(nums, target)




num1 = [1, 2,3,4]
# num2=num1
# num2.append(5)
# print num2,num1
target1= 10

print fourSum(num1, target1)
print

#
# a=[1,2,3]
#
# b=[1,3,2]
#
# c=[1,3,2]
#
# d=[]
# d.append(a)
# d.append(b)
# d.append(c)
#
# print set(d)
# Traceback (most recent call last):
#   File "H:/LearnSth/LeetCode/venv/18_un.py", line 30, in <module>
#     print set(d)
# TypeError: unhashable type: 'list'



e=[1,2,1,2,3,4]
print set(e)

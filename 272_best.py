# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """

        sortlist=[]
        self.inorder(root,sortlist)
        res=self.findK(k,target,sortlist)
        return res

    def inorder(self,root,res):
        if root==None:
            return
        self.inorder(root.left,res)
        res.append(root.val)
        self.inorder(root.right,res)

    def findK(self,k,target,sortlist):
        id=-1
        for i in range(len(sortlist)):
            if sortlist[i]>target:
                id=i
                break
        if id==-1:
            q=len(sortlist)
            p=q-1
        else:
            p=id-1
            q=id
        num=0
        res=[]
        print(p,q)
        while (p>=0 or q<len(sortlist)) and num<k:
            leftdiff=abs(sortlist[p]-target) if p>=0 else float("inf")
            rightdiff=abs(sortlist[q]-target) if q<len(sortlist) else float("inf")
            if leftdiff<rightdiff:
                res.append(sortlist[p])
                p-=1
            else:
                res.append(sortlist[q])
                q+=1
            num+=1
        return res








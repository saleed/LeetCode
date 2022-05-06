# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        res=[]
        self.inorder(root,res)
        preval=0
        for i in range(len(res))[::-1]:
            res[i].val=preval+res[i].val
            preval=res[i].val


        return root



    def inorder(self,root,res):
        if root==None:
            return
        self.inorder(root.left,res)
        res.append(root)
        self.inorder(root.right,res)






###思路错误
    def dfs(self,root,father,fatherMoreThanRoot):
        if root==None:
            return 0

        if father!=None and root.val<father.val:
            rval = self.dfs(root.right, root, fatherMoreThanRoot+root.val)
            lval= self.dfs(root.left,root,fatherMoreThanRoot+root.val+rval)
        else:
            rval= self.dfs(root.right,root,0)
            lval=self.dfs(root.left,root,root.val+rval)
        tmp=root.val
        root.val=fatherMoreThanRoot+root.val+rval
        return tmp+rval+lval




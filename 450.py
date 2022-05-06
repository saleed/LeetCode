# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        father=TreeNode(float("inf"))
        father.left=root
        self.deleteNodeFather(father.left,father,0,key)
        return father.left

    def deleteNodeFather(self,root,father,lr,key):
        if root==None:
            return
        if root.val==key:
            nextNode=None
            if root.left==None and root.right==None:
                nextNode=None
            elif root.left==None:
                nextNode=root.right
            elif root.right==None:
                nextNode=root.left
            else:
                p=root.right
                while p.left!=None:
                    p=p.left
                p.left=root.left
                nextNode=root.right
                root.left=None

            if lr==0:
                father.left=nextNode
            else:
                father.right=nextNode

        elif root.val<key:
            self.deleteNodeFather(root.right,root,1,key)
        else:
            self.deleteNodeFather(root.left,root,0,key)


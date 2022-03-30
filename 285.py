# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """


        prenode=None

        dst=root

        while dst!=None and  dst!=p:
            if dst.val<p.val:
                dst=dst.left

            elif dst.val>p.val:
                dst=dst.right
            else:
                continue
            prenode=dst
        if dst==None:
            return None

        if dst.right!=None:
            q=dst.right
            while q.left!=None:
                q=q.left
            return q
        else:
            return prenode








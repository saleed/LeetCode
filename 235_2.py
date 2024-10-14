# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



#题意理解错误
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val>q.val:
            p,q=q,p
        if root==None:
            return None
        if root!=None:
            if root.val==p and root.val==q:
                return root
            elif root.val==p and self.lowestCommonAncestor(root.right,q,q)!=None:
                return root
            elif root.val==q and self.lowestCommonAncestor(root.left,p,p)!=None:
                return root
            elif root.val>p and root.val<q and self.lowestCommonAncestor(root.left,p,p)!=None and self.lowestCommonAncestor(root.right,q,q)!=None:
                return root
            elif root.val<p:
                return self.lowestCommonAncestor(root.right,p,q)
            elif root.val>q:
                return self.lowestCommonAncestor(root.left,p,q)
            else:
                return None


##理解错误题意

    def setExistIn(self,root,s):
        if root==None:
            return None
        if len(s)==0:
            return root
        if root.val in s:
            s.remove(root.val)
            left=self.setExistIn(root.left,s)
            right=self.setExistIn(root.right,s)
            s.add(root.val)
            if left!=None or right!=None:
                return root

        return None
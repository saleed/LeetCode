# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        self.inorder2(root,res)
        return res


    def inorder(self,root,res):
        if root==None:
            return
        self.inorder(root.left,res)
        res.append(root.val)
        self.inorder(root.right,res)


    def inorder2(self,root,res):

        st=[]
        p=root
        while p!=None or len(st)>0:
            if p!=None:
                st.append(p)
                p=p.left
            else:
                top=st.pop()
                res.append(top.val)
                p=top.right












# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root==None:
            return []
        res=[]
        # self.recursive(root,res)
        # return res

        self.postorder(root,res)
        return res

    def recursive(self,root,res):
        if root==None:
            return
        self.recursive(root.left,res)
        self.recursive(root.right,res)
        res.append(root.val)

    def postorder(self,root,res):
        st=[root]
        while len(st)>0:
            top=st[-1]
            if top.right!=None:
                st.append(top.right)
            if top.left!=None:
                st.append(top.left)
                k=1
            if top.left==None and top.right==None:
                res.append(top.val)
                st.pop()
        return res


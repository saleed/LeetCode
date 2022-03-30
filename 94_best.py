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
        res = self.noRecursiveInorder2(root)
        return res

    def inorder(self, root, res):
        if root == None:
            return
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)


    def noRecursiveInorder(self,root):
        st=[]
        res=[]
        p=root
        while p!=None or len(st)>0:
            while p!=None:
                st.append(p)
                p=p.left
            top=st.pop()
            res.append(top.val)
            if top.right!=None:
                p=top.right

        return res

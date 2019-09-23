# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.inorder(root)



    def inorder(self,root):
        if root==None:
            return []

        node=root
        st=[]
        res=[]
        while node!=None or len(st)>0:
            if node.left!=None:
                st.append(node)
                node=node.left
            else:
                res.append(node.val)
                if node.right==None:
                    node=st.pop()
                else:
                    node=node.right





    def inorder2(self,root):
        if root==None:
            return []


        st=[]
        res=[]
        while root!=None or len(st)>0:
            if root==None:
                root=st.pop()
                res.append(root.val)
                root=root.right
            else:
                st.append(root)
                root=root.left




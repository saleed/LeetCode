# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.recursive(root)

    def recursive(self,root):

        st=[]
        res=[]
        node=root

        while node!=None or len(st)>0:
            while node:
                res.append(node.val)
                if node.right!=None:
                    st.append(node.right)
                node=node.left
            if len(st)==0:
                return res
            node=st.pop()
        return res


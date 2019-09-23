# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root==None:
            return []
        st=[root]
        res=[]
        while len(st)>0:
            res.append(st[-1].val)
            stbackup=st[:]
            st=[]
            for i in stbackup:
                if i.left!=None:
                    st.append(i.left)
                if i.right!=None:
                    st.append(i.right)
        return res
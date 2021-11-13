# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        return self.interation(root)

    def interation(self,root):
        if root==None:
            return []
        res=[]
        st=[[root,0]]
        while len(st)>0:
            top=st[-1]
            if top[1]==2:
                res.append(top[0].val)
                st.pop()
            elif top[1]==1:
                st[-1][1]=2
                if top[0].right!=None:
                    st.append([top[0].right,0])
            else:
                st[-1][1]=1
                if top[0].left!=None:
                    st.append([top[0].left,0])
        return res






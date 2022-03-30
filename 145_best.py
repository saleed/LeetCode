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
        if root==None:
            return None
        return self.colorPostOrder(root)

    def postOrderIteration(self,root):
        st=[root]
        res=[]
        while len(st)>0:
            top=st.pop()
            res=[top.val]+res
            if top.left!=None:
                st.append(top.left)
            if top.right!=None:
                st.append(top.right)
        return res



    def colorPostOrder(self,root):
        st=[[root,0]]
        res=[]
        while len(st)>0:
            top=st[-1]
            if top[0]!=None:
                if top[1]==0:
                    st[-1][1]=1
                    st.append([top[0].left,0])
                elif top[1]==1:
                    st[-1][1]=2
                    st.append([top[0].right,0])
                else:
                    res.append(top.val)
                    st.pop()
            else:
                st.pop()

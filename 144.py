# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # res=[]
        # self.recursive(root,[])
        # return res

        return self.iteration2(root)

    def recursive(self,root,res):
        if root!=None:
            res.append(root.val)
        self.recursive(root.left,res)
        self.recursive(root.right,res)


    def iteration(self,root):
        if root==None:
            return None
        st=[root]
        res=[]
        while len(st)>0:
            top=st.pop()
            if top.right!=None:
                st.append(top.right)
            if top.left!=None:
                st.append(top.left)
            res.append(top.val)
        return res

    def iteration2(self,root):
        if root==None:
            return []
        st=[]
        p=root
        res=[]
        while p!=None or len(st)>0:
            while p!=None:
                res.append(p.val)
                if p.right!=None:
                    st.append(p.right)
                p=p.left
            if len(st)>0:
                p=st.pop()

        return res



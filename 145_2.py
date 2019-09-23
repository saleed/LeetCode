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
        return self.interative(root)


    def interative(self,root):
        if root==None:
            return []
        vis=set()
        st=[root]
        res=[]
        while len(st)>0:
            tmp=st[-1]
            if tmp in vis:
                res.append(st.pop())
            else:
                if tmp.right == None and tmp.left == None:
                    res.append(st.pop())
                ##必须要先把右子树进栈，然后再入左子树
                if tmp.right!=None:
                    st.append(tmp.right)
                if tmp.left!=None:
                    st.append(tmp.left)
                vis.add(tmp)
        return res










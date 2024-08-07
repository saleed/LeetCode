[]# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        p=root
        st=[]
        res=[]
        swapnode=[]
        first=None
        second=None
        while p!=None or len(st)>0:
            if p==None:
                top=st.pop()
                p=top.right
                if len(res)>0 and top.val<res[-1]:
                    if first is None:
                        first=top
                    else:
                        second=pre
                res.append(top.val)

            else:
                st.append(p)

                p=p.left


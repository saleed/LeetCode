# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """

        ptr=root
        self.res=[]
        st=[]
        while ptr!=None or len(st)!=0:
            if ptr!=None:
                st.append(ptr)
                ptr=ptr.left
            else:
                top=st.pop()
                self.res.append(top)
                ptr=top.right
        self.index=0

    def next(self):
        """
        :rtype: int
        """
        if self.index==len(self.res):
            return 0
        v=self.res[self.index]
        self.index+=1
        return v

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index!=self.index



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
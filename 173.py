# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.res=list(reversed(self.recursive(root)))

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if len(self.res)>0:
            return self.res.pop()


    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if len(self.res)>0:
            return True
        else:
            return False


    def recursive(self, root, res):
        if root == None:
            return
        res.append(root.val)
        self.preorder(root.left, res)
        self.preorder(root.right, res)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
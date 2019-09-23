# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        curstr=""
        res=[]
        self.dfs(curstr,res,root)
        return res



    def dfs(self,curstr,res,root):
        if root==None:
            return
        newstr = curstr[:]
        if newstr == "":
            newstr += str(root.val)
        else:
            newstr += "->" + str(root.val)

        if root.left==None and root.right==None:
            res.append(newstr)
        else:
            self.dfs(newstr,res,root.left)
            self.dfs(newstr,res,root.right)
        return


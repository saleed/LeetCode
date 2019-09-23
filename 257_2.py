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
        if root==None:
            return []
        res=[]
        self.dfs(root,[],res)
        strres=[]
        for i in res:
            if len(i)>0:
                cur=""
                for j in i:
                    cur+=str(j)+"->"
                strres.append(cur[:-1])
        return strres




    def dfs(self,root,path,res):
        if root==None:
            return
        path.append(root.val)
        if root.left==None and root.right==None:
            res.append(path[:])
        else:
            self.dfs(root.left,path,res)
            self.dfs(root.right,path,res)
        path.pop()
        return


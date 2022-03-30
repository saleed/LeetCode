class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res=[-float("inf")]
        self.recursive(root,res)
        return res[0]



    def recursive(self,root,res):
        if root==None:
            return 0

        lres=self.recursive(root.left,res)
        rres=self.recursive(root.right,res)
        res[0]=max(res[0],root.val+max(0,lres)+max(0,rres))
        return root.val+max(0,lres,rres)

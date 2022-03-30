# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        return self.iteration(root,target)


    def iteration(self,root,target):
        closest=float("inf")
        while root:
            print(closest)
            if abs(root.val-target)<closest:
                closest=root.val
            if root.val<target:
                root=root.right
            elif root.val>target:
                root=root.left
            else:
                return root.val
        return closest




    def dfs(self,root,target):
        if root == None:
            return float("inf"), None
        else:
            if root.val == target:
                return 0, root
            if root.val > target:
                diff, node = self.dfs(root.left, target)
                if diff < abs(root.val - target):
                    return diff, node
                else:
                    return abs(root.val - target), root
            else:
                diff, node = self.dfs(root.right, target)
                if diff < abs(root.val - target):
                    return diff, node
                else:
                    return abs(root.val - target), root
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        res = []
        self.recursive({}, root, res)

        return res

    def recursive(self, subdict, root, res):
        if root == None:
            return ["#"]

        left = self.recursive(subdict, root.left, res)
        right = self.recursive(subdict, root.right, res)

        tmp = [root.val]
        tmp.extend(left)
        tmp.extend(right)
        print(tmp)
        key=tuple(tmp)
        if key in subdict:
            if subdict[key]==1:
                res.append(root)
                subdict[key]+=1
        else:
            subdict[key]=1

        return tmp


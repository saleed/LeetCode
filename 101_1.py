# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """


    def ismiorr(self,left,right):
        if left==right==None:
            return True
        if left!=None and right!=None



    def level_compare(self,root):
        if root == None:
            return True
        left = [root.left]
        right = [root.right]
        while len(left) == len(right) and len(left) > 0:
            p = 0
            q = len(left) - 1
            newleft = []
            newright = []

            while q >= 0:
                if (left[p] == None and right[q] == None) or (
                        left[p] != None and right[q] != None and left[p].val == right[q].val):
                    if left[p] != None:
                        newleft.append(left[p].left)
                        newleft.append(left[p].right)
                    if right[p] != None: ##注意这里不是q,是顺序左到右取节点！！！
                        newright.append(right[p].left)
                        newright.append(right[p].right)
                    p += 1
                    q -= 1
                else:

                    # print(len(left),p,q)
                    # print(left,right)
                    return False
            left = newleft
            right = newright
        return True


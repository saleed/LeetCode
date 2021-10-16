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

        layer=[root]
        while len(layer)>0:
            if self.same(layer):
                newlayer=[]
                for v in layer:
                    if v==None:
                        continue
                    newlayer.append(v.left)
                    newlayer.append(v.right)
                layer=newlayer
            else:
                return False
        return True



    def same(self,plist):
        p=len(plist)-1
        q=0
        while q<=p:
            if(plist[p]==None and plist[q]==None) or(plist[p]!=None and plist[q]!=None and plist[p].val==plist[q].val):
                q+=1
                p-=1
                continue
            else:
                return False
        return True



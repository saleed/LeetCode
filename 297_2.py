# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root==None:
            return []
        res=[root.val]
        level=[root]
        while len(level)>0:
            nextlevel=[]
            for node in level:
                if node!=None:
                    res.append(node.val)
                    nextlevel.append(node.left)
                    nextlevel.append(node.right)
                else:
                    res.append(None)
            level=nextlevel
        return res



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data)==0:
            return None
        root=TreeNode(data[0])
        p=0
        level=[root]
        while len(level)>0:
            nextlevel=[]
            for i in level:
                if i==None:
                    continue
                else:
                    if p==len(data)-1:
                        i.left=None
                        i.right=None
                        continue
                    p+=1
                    if data[p]==None:
                        i.left=None
                    else:
                        i.left=TreeNode(data[p])
                    nextlevel.append(i.left)
                    if p==len(data)-1:
                        break
                    p+=1
                    if data[p]==None:
                        i.right=None
                    else:
                        i.right=TreeNode(data[p])
                    nextlevel.append(i.right)
            level=nextlevel
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
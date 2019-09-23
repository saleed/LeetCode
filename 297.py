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
        res=[]
        childbuffer=[]
        if root==None:
            return []
        childbuffer.append(root)
        while len(childbuffer)>0:
            print res
            newbuf=[]
            for i in childbuffer:
                if i==None:
                    res.append(None)
                    continue
                else:
                    res.append(i.val)
                    newbuf.append(i.left)
                    newbuf.append(i.right)
            childbuffer=newbuf
            allNone=True
            for i in childbuffer:
                if i!=None:
                    allNone=False
            if allNone:
                break
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data)==0 or data[0]==None:
            return None
        root=TreeNode(data[0])
        buf=[root]
        l=1
        while len(buf) and l<len(data):
            newbuf=[]
            for i in buf:
                if i.val==None:
                    continue
                else:
                    i.left=TreeNode(data[l])
                    newbuf.append(i.left)
                    l+=1
                    if l>=len(data):
                        break
                    i.right=TreeNode(data[l])
                    newbuf.append(i.right)
                    l+=1
        return root




# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
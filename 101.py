    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None

    class Solution(object):
        def isSymmetric(self, root):
            """
            :type root: TreeNode
            :rtype: bool
            """
            if root==None:
                return True
            return self.ismirror(root.left,root.right)




        def levelTranversal(self,root):
            curlevel=[root]
            while len(curlevel)>0:
                if not self.symmetric(curlevel):
                    return False
                nextlevel=[]
                for node in curlevel:
                    if node==None:
                        continue
                    nextlevel.append(node.left)
                    nextlevel.append(node.right)
                curlevel=nextlevel
            return True
        def symmetric(self,nodes):
            p=0
            q=len(nodes)-1
            while p<q:
                if (nodes[p]==None and nodes[q]==None) or (nodes[p]!=None and nodes[q]!=None and nodes[p].val==nodes[q].val):
                    p+=1
                    q-=1
                else:
                    return False
            return True


        def ismirror(self,p,q):
            if p==None and q==None:
                return True
            if p!=None and q!=None and p.val==q.val:
                return self.ismirror(p.left,q.right) and self.ismirror(p.right,q.left)
            return False




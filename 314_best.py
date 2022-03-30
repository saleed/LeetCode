# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # resdict={}
        # minpos,maxpos=self.dfs(resdict,root,0)
        #
        # res=[]
        # for v in range(minpos,maxpos+1):
        #     if v in resdict:
        #         res.append(resdict[v])
        # return res
        if root==None:
            return None

        return self.levelFind(root)


    def levelFind(self,root):

        nodeList=[[root,0]]
        resdict={}
        minv=0
        maxv=0
        while len(nodeList)>0:
            newlist=[]
            for node in nodeList:
                if node[1] in resdict:
                    resdict[node[1]].append(node[0].val)

                else:
                    resdict[node[1]]=[node[0].val]
                if node[0].left!=None:
                    newlist.append([node[0].left,node[1]-1])

                if node[0].right != None:
                    newlist.append([node[0].right, node[1] +1])

                minv=min(node[1],minv)
                maxv=max(node[1],maxv)
            nodeList=newlist
        res=[]
        for v in range(minv,maxv+1):
            if v in resdict:
                res.append(resdict[v])
        return res








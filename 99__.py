# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root==None:
            return

        nodelist=[]
        p=root
        st=[]
        while len(st)>0 or p!=None:
            if p!=None:
                st.append(p)
                p=p.left
            else:
                top=st.pop()
                nodelist.append(top)
                p=top.right
        start=0
        end=0
        i=1
        while i<len(nodelist):
           if nodelist[i].val<nodelist[i-1].val:
               start=i-1
               break
           else:
               i+=1
        i+=1
        while i<len(nodelist):
            if nodelist[i].val < nodelist[i - 1].val:
                end = i
                break
            else:
                i += 1

        if i==len(nodelist):
            end=i

        print(nodelist)
        print(start,end)

        nodelist[start].val,nodelist[end].val=nodelist[end].val,nodelist[start].val








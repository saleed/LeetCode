# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.iterative2(root)





    #访问一个根节点，先后保存右左节点，然后迭代访问栈顶
    def iterative1(self, root):
        if root == None:
            return []
        res = []
        st = [root]
        while len(st) > 0:
            tmp = st.pop()
            res.append(tmp.val)
            if tmp.right != None:
                st.append(tmp.right)
            if tmp.left != None:
                st.append(tmp.left)
        return res

    #迭代访问栈顶节点，对每个栈顶，穷尽搜索其左子节点并将右子节点入栈
    def iterative2(self,root):
        if root==None:
            return []
        res=[]
        st=[root]
        while len(st)>0:
            tmp=st.pop()
            while tmp!=None:
                res.append(tmp.val)
                st.append(tmp.right)
                tmp=tmp.left

        return res









    def recursive(self,root,res):
        if root==None:
            return
        res.append(root.val)
        self.recursive(root.left)
        self.recursive(root.right)



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.inorder(root)

    def inorder(self,root):
        if root==None:
            return []
        st=[]
        res=[]
        node=root
        #方法1：
        while node!=None or len(st)>0:
            if node==None:
                top=st.pop()
                res.append(top.val)
                node=top.right
            else:
                st.append(node)
                node=node.left
        return res

        #方法2：

        # while (!path.empty()) {
        # auto node = path.top();
        # path.pop();
        # res.push_back(node->val);
        # // 每 pop 一个节点，将其右子树做 ** 左臂入栈 ** 操作。
        # node = node->right;
        # while (node) {
        # path.push(node);
        # node = node->left;




    def inorderTraversal(self, root):
        r, stack = [], []
        while True:  #这个条件应该是root!=None or len(stack)>0
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return r
            node = stack.pop()
            r.append(node.val)
            root = node.right
        return r







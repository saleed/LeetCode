
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.interative(root)

    def interative(self, root):
        if root == None:
            return []
        res = []
        state = {}
        state[root] = 0
        st = [root]
        while len(st) > 0:
            top = st[-1]
            if state[top] == 0:
                if top.left != None:
                    st.append(top.left)
                    state[top.left] = 0
                state[top] = 1

            elif state[top] == 1:
                if top.right != None:
                    st.append(top.right)
                    state[top.right] = 0
                state[top] = 2
            else:
                res.append(top.val)
                st.pop()
        return res







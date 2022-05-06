# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if len(s)==0:
            return None
        p=0
        while p<len(s):
            if s[p]=='(':
                break
            p+=1
        rootstr=s[:p]
        print(rootstr)
        tmproot=TreeNode(int(s[:p]))
        if p==len(s):
            return tmproot
        p+=1
        st=["("]
        while not len(st)==0:
            if s[p]=="(":
                st.append("(")
            elif s[p]==")":
                st.pop()
            p+=1
        left=s[len(rootstr)+1:p-1]
        right=s[p+1:-1]
        print left,right
        tmproot.left=self.str2tree(left)
        tmproot.right=self.str2tree(right)
        return tmproot




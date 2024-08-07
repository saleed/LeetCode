# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None




###关于递归的写法有两种类型:
# 1.保存中间信息，在结束条件满足情况下结算，递归过程中类似于穷举搜索
# 2.回溯的思想，整个函数的输出值为结果，在结束条件达到后，往前一层回直到顶层，递归过程更像独立的分治
#####
#此题不适合第二种思路，只能第一种思路，记录搜索中间值

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.Solve(root)


#以下是第二种递归的写法
    def dfs(self,root,acc):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return root.val+acc*10
        if root.left==None:
            return self.dfs(root.right,root.val+acc*10)
        if root.right==None:
            return self.dfs(root.left,root.val+acc*10)
        return self.dfs(root.left,root.val+acc*10)+self.dfs(root.right,root.val+acc*10)


    def topToBottom(self,root,res,cur):
        if root==None:
            return
        if root.left==None and root.right==None:
            cur.append(root.val)
            res.append(cur[:])
            cur.pop()
            return
        cur.append(root.val)
        self.topToBottom(root.left,res,cur)
        self.topToBottom(root.right,res,cur)
        cur.pop()
        return



    def Solve(self,root):

        res=[]
        self.topToBottom(root,res,[])

        acc=0
        for l in res:
            acc+=self.listToDigit(l)
        return acc

    def listToDigit(self,ll):
        res=0
        for l in ll:
            res=res*10+l
        return res








    #总结：如果产生思路：

    #首先想想看是否可以通过递归解决
        # 1.找父子递归关系
        # 2.递归过程中需要保存哪些中间量：累积值
        # 3.递归中止条件

a=Solution()


test=[1, 2, 3]
print(a.listToDigit(test))



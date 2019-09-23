class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        self.dfs(n,n,"",res)
        return res
#
# 递归思路：
# 统计剩余左右可填括号的数目
# 如果左右均剩余0，则输出一个可行解
# 如果左剩余0，只能添加右括号
# 如果左不为0，且左右括号剩余数目相等，则只能添加一个左括号，反之，既可以加左又可以加右


    def dfs(self,left,right,curstr,res):
        if left==0 and right==0:
            res.append(curstr[:])
            return
        elif left==0:
            curstr+=')'
            self.dfs(left,right-1,curstr,res)
        elif left==right:
            curstr+='('
            self.dfs(left-1,right,curstr,res)
        else:
            curstr+='('
            self.dfs(left-1,right,curstr,res)
            curstr=curstr[:-1]
            curstr+=')'
            self.dfs(left,right-1,curstr,res)








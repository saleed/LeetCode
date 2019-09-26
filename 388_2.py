#解法1：构造一棵树，多叉树，然后对数使用递归深度遍历，求最大深度，比较麻烦，容易理解
#解法2：DFS思想，使用栈保存当前父目录的深度和路径长度
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        stack=[]
        id=0
        maxlen=0
        while id<len(input):
            ptr=id
            while input[ptr]!='\n' and ptr<len(input):
                ptr+=1
            if ptr==len(input):



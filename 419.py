class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """

        if len(board)==0 or len(board[0])==0:
            return 0
        res=0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i>0 and board[i-1][j]=='X':
                    continue
                if j>0 and board[i][j-1]=='X':
                    continue
                if board[i][j]=='X':
                    res+=1
        return res

    # 无效样例:
    #
    # ...
    # X
    # XXXX
    # ...
    # X
    # 你不会收到这样的无效甲板 - 因为战舰之间至少会有一个空位将它们分开。

    #注意这个题目由有测试用例限制，假如没有这个限制，需要判断无效场景
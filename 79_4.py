class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        exist=[[[False for _ in range(len(word))] for _ in range(len(board[0]))] for _ in range(len(board))]




    def dfs(self,i,j,k):
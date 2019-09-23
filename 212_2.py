class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie=Trie()

        res=[]
        for word in words:
            self.generateTrieTree(board, trie, word)

        return res

    #使用DFS超时，因此使用
    def generateTrieTree(self,board,trie,word):

        vis=[[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(trie,board,"",vis,i,j)

        if trie.search(word) == True:
            res.append(word)


    def dfs(self,trie,board,cur,vis,x,y,targetLen):
        if len(cur)==targetLen:
            trie.insert(cur[:])
            return
        if x<len(board) and x>=0 and y<len(board[0]) and y>=0 and vis[x][y]==0:
            newcur=cur+board[x][y]
            vis[x][y]=1
            # print(newcur)
            # trie.insert(newcur)
            dx=[1,0,-1,0]
            dy=[0,1,0,-1]
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                self.dfs(trie,board,newcur,vis,nx,ny)
            vis[x][y]=0
        return




class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.child = [None] * 27

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        for i in word:
            if self.child[ord(i.lower()) - ord('a')] != None:
                self = self.child[ord(i.lower()) - ord('a')]
            else:
                Node = Trie()
                self.child[ord(i.lower()) - ord('a')] = Node
                self = Node
        self.child[26] = 0

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        for i in word:
            if self.child[ord(i.lower()) - ord('a')] == None:
                return False
            self = self.child[ord(i.lower()) - ord('a')]
        return self.child[26] == 0

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        for i in prefix:
            if self.child[ord(i.lower()) - ord('a')] == None:
                return False
            self = self.child[ord(i.lower()) - ord('a')]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
a=Solution()
b=[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
w=["oath","pea","eat","rain"]
print(a.findWords(b,w))
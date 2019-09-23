
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
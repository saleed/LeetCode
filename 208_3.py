class Trie(object):



###还需要深刻理解，字典树是每条边对应一个字母，而不是一个节点！！！！
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.alpha=[None]*27

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        if len(word)==0:
            return
        for s in word:
            if self.alpha[int(ord(s.lower())-ord('a'))]==None:
                self.alpha[int(ord(s.lower())-ord('a'))]=Trie()
            self=self.alpha[ord(s.lower())-ord('a')]
        self.alpha[26]=0
        return




    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        for s in word:
            if self.alpha[int(ord(s.lower())-ord('a'))]!=None:
                self=self.alpha[int(ord(s.lower())-ord('a'))]
            else:
                return False
        return self.alpha[26]==0

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        for s in prefix:
            if self.alpha[int(ord(s.lower())-ord('a'))]!=None:
                self=self.alpha[int(ord(s.lower())-ord('a'))]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

print(None==0)
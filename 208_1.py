class Trie(object):

    def __init__(self):
        self.wordRoot={}

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        if len(word)>0:
            head=word[0]
            if head not in self.wordRoot:
                self.wordRoot[head]=Trie()
            self.wordRoot[head].insert(word[1:])
        else:
            self.wordRoot["end"]=1


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word)==0 and "end" in self.wordRoot:
            return True
        if word[0] in self.wordRoot:
            return self.wordRoot[word[0]].search(word[1:])
        else:
            return False

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        if len(prefix)==0:
            return True
        if prefix[0] in self.wordRoot:
            return self.wordRoot[prefix[0]].search(prefix[1:])
        else:
            return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
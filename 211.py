class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic=[None]*27

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        p=self
        for i in range(len(word)):
            if p.dic[ord(word[i])-ord('a')]!=None: #be careful for this is very important
                p=p.dic[ord(word[i]) - ord('a')]
            else:
                newTrie=WordDictionary()
                p.dic[ord(word[i])-ord('a')]=newTrie
                p=newTrie
        p.dic[26]=WordDictionary()

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        p = self
        for i in range(len(word)):
            if word[i]!='.':
                if p.dic[ord(word[i]) - ord('a')] != None:
                    p = p.dic[ord(word[i]) - ord('a')]
                else:
                    return False
            else:
                newword=word[i+1:]
                p = self
                for i in range(26):
                    if p.dic[i]!=None:
                        self=p.dic[i]
                        if self.search(newword):
                            return True
                return False
        if p.dic[26] != None:
            return True
        else:
            return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
class WordDictionary(object):

    def __init__(self):
        self.wd = {}

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        if len(word) == 0:
            self.wd["end"] = 1
        else:
            if word[0] not in self.wd.keys():
                a=WordDictionary()
                self.wd[word[0]] = a
            self.wd[word[0]].addWord(word[1:])

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 0 and "end" in self.wd.keys():
            return True
        else:
            if len(word) > 0:
                if word[0] in self.wd.keys():
                    return self.wd[word[0]].search(word[1:])
                if word[0] == ".":
                    for k in self.wd.keys():
                        if k == "end":
                            continue
                        if self.wd[k].search(word[1:]):
                            return True
                    return False
            return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


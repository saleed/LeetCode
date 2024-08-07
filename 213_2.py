class WordDistance(object):

    def __init__(self, wordsDict):
        """
        :type wordsDict: List[str]
        """
        self.dict=wordsDict
        self.shortestdict={}


    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if (word1,word2) in self.shortestdict:
            return self.shortestdict[(word1,word2)]
        else:
            pos1=float("inf")
            pos2=-float("inf")
            mind=float("inf")
            for i in range(len(self.dict)):
                if self.dict[i]==word1:
                    pos1=i
                if self.dict[i]==word2:
                    pos2=i
                mind=min(mind,abs(pos1-pos2))
            self.shortestdict[(word1,word2)]=mind
            self.shortestdict[(word2,word1)]=mind
        return mind



# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
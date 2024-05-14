class WordDistance(object):

    def __init__(self, wordsDict):
        """
        :type wordsDict: List[str]
        """
        self.dict={}
        for i in range(len(wordsDict)):
            if wordsDict[i] in self.dict:
                self.dict[wordsDict[i]].append(i)
            else:
                self.dict[wordsDict[i]]=[i]

        for k in self.dict:
            self.dict[k].sort()
        self.mindist={}

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1+"_"+word2 in self.mindist:
            return self.mindist["word1"+"_"+"word2"]
        if word2+"_"+word1 in self.mindist:
            return self.mindist["word2"+"_"+"word1"]


        q=0
        p=0
        mindist=float("inf")
        while q<len(self.dict[word2]):
            v2=self.dict[word2][q]
            while p<=len(self.dict[word1]):
                v1=self.dict[word1][p] if p==len(self.dict[word1]) else float("inf")
                prev1=self.dict[word1][p-1] if p>0 else -float("inf")
                if v2<=v1 and v2>=prev1:
                    mindist=min(mindist,abs(v2-v1),abs(v2-prev1))
                    break
                p+=1
            q+=1

        self.mindist["word2" + "_" + "word1"]=mindist
        self.mindist["word1" + "_" + "word2"]=mindist

        return mindist


    def shortest2(self,word1,word2):




# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
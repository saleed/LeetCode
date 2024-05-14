class WordDistance(object):
    def __init__(self, wordsDict):
        """
        :type wordsDict: List[str]
        """
        self.wdist={}
        self.mindist={}
        for i in range(len(wordsDict)):
            self.wdist[wordsDict[i]]=i
            # print("ppp",p)
            for k in self.wdist:
                p=wordsDict[i]
                q=k
                if p>q:
                    p,q=q,p
                # print("pq",p,q)
                if (p,q) in self.mindist:
                    self.mindist[p+q]=min(self.mindist[(p,q)],abs(self.wdist[p]-self.wdist[q]))
                else:
                    self.mindist[p+q]=abs(self.wdist[p]-self.wdist[q])
            # print(self.mindist)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1>word2:
            word1,word2=word2,word1
        # print(self.mindist)
        # print(self.wdist)
        return self.mindist[word1+word2]



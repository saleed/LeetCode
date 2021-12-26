class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        posdict={}
        for i in range(len(wordsDict)):
            if wordsDict[i] in posdict:
                posdict[wordsDict[i]].append(i)
            else:
                posdict[wordsDict[i]]=[i]


        p=0
        q=0
        mindist=float("inf")
        while q<len(posdict[word2]):
            v2=posdict[word2][q]
            while p<=len(posdict[word1]):
                v1=posdict[word1][p] if p<len(posdict[word1]) else float("inf")
                prev1=posdict[word1][p-1] if p>0 else -float("inf")
                if v2>=prev1 and v2<=v1:
                    mindist=min(mindist,abs(v2-prev1),abs(v2-v1))
                    break
                p+=1
            q+=1
        return mindist



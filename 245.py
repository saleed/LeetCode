class Solution(object):
    def shortestWordDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """


        posdict = {}
        for i in range(len(wordsDict)):
            if wordsDict[i] in posdict:
                posdict[wordsDict[i]].append(i)
            else:
                posdict[wordsDict[i]] = [i]

        p = 0
        q = 0
        mindist = float("inf")
        while q < len(posdict[word2]):
            v2 = posdict[word2][q]
            while p < len(posdict[word1]):
                v1 = posdict[word1][p]
                if v1<v2:
                    mindist = min(mindist, abs(v2 - v1))
                    p+=1
                else:
                    break

            q += 1
        return mindist
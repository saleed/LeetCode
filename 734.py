class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2, similarPairs):
        """
        :type sentence1: List[str]
        :type sentence2: List[str]
        :type similarPairs: List[List[str]]
        :rtype: bool
        """
        similarset=set()
        for v in similarPairs:
            similarset.add(v[0]+"_"+v[1])
            similarset.add(v[1]+"_"+v[0])

        if len(sentence1)!=len(sentence2):
            return False
        for i in range(len(sentence1)):
            if sentence2[i]+"_"+ sentence1[i] in similarset or sentence1[i]+"_"+ sentence2[i] in similarset or sentence1[i]==sentence2[i]:
                continue
            else:
                return False

        return True


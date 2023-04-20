class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """

        worddict={}
        for w in words:
            worddict[w]=worddict[w]+1 if w in worddict else 1
        wordlist=[]
        for k in worddict:
            wordlist.append([k,worddict[k]])


        wordlist.sort(key=lambda x:(x[0],x[1]))
        res=[]
        for i in range(min(k,len(wordlist))):
            res.append(wordlist[i][0])
        return res





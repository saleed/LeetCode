class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        dict={}
        for i in range(len(words)):
            dict[words[i]]=i
        res=[]
        for w in range(len(words)):
            for i in range(len(words[w])):
                if i<

                    if curword[::-1] in dict.keys():
                        res.append([w,dict[curword[::-1]]])




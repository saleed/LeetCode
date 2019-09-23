class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res=[]
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i]+words[j]==(words[i]+words[j])[::-1]:
                    res.append([i,j])
                if words[j] + words[i] == (words[j]+words[i])[::-1]:
                    res.append([j, i])
        return res


s="abc"
print(s[::-1])
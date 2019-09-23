class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        maxval=-1
        setlist=[]
        for word in words:
            setlist.append(set(word))
        for i in range(len(words)):
            for j in range(len(setlist)):
                if self.wordInLetterSet(words[i],setlist[j]):
                    continue
                else:
                    maxval=max(maxval,len(words[i])*len(words[j]))
        return maxval if maxval!=-1 else 0


    def wordInLetterSet(self,word,s):
        for i in word:
            if i in s:
                return True
        return False
Input=["abcw","baz","foo","bar","xtfn","abcdef"]
a=Solution()
print a.maxProduct(Input)
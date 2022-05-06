class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        keyword=["qwertyuiop","asdfghjkl","zxcvbnm"]
        res=[]
        for w in words:
            for s in keyword:
                # print(w,s)
                if self.contain(w,s):
                    res.append(w)
                    break
        return res

    def contain(self,s1,s2):
        for v in s1:
            if v.lower() in s2:
                continue
            else:
                return False

        return True
test=["Hello","Alaska","Dad","Peace"]

ss=Solution()
print(ss.findWords(test))
print(ss.contain("elo",test[0])  )
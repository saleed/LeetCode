class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """

        for i in range(len(words)):
            for j in range(len(words[i])):
                if j<len(words) and i<len(words[j]) and words[i][j]==words[j][i]:
                    continue
                return False
        return True
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1=="" or word2=="":
            return max(len(word1),len(word2))
        dp=[[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

        for i in range(len(word1)+1):
            dp[i][0]=i
        for j in range(len(word2)+1):
            dp[0][j]=j

        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                v1 = dp[i - 1][j]
                v2 =dp[i][j - 1]
                v3 = dp[i - 1][j - 1]
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=min(v1+1,v2+1,v3)
                else:
                    dp[i][j]=min(v1,v2,v3)+1

        return dp[-1][-1]
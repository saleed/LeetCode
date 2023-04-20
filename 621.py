class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        ttype=set(tasks)
        for i in range(len(tasks)):
            for j in range(len(ttype)):
                dp[i][j]=dp
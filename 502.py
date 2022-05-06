class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """

        dp = [[0 for _ in range(w+1)] for _ in range(k)]


k=2
w=0
profit=[1,2,3]
capital=[0,1,1]

ss=Solution()
print(ss.findMaximizedCapital(k,w,profit,capital))
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        for i in range(len(citations)):
            if citations[i]>=len(citations)-i:
                return len(citations)-i
        return 0


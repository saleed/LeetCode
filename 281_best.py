class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        res=[v1,v2]
        self.vec=res
        self.index=0

    def next(self):
        """
        :rtype: int
        """
        r=self.index/len(self.vec)
        col=self.index%(len(self.vec[]))
    def hasNext(self):
        """
        :rtype: bool
        """

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
class Vector2D(object):

    def __init__(self, vec):
        """
        :type vec: List[List[int]]
        """
        self.ptr=0
        self.vecList=[]
        for v in vec:
            self.vecList.extend(v)

    def next(self):
        """
        :rtype: int
        """
        val=self.vecList[self.ptr]
        self.ptr+=1
        return val


    def hasNext(self):
        """
        :rtype: bool
        """
        if self.ptr==len(self.vecList):
            return False
        else:
            return True


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
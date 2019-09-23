class MedianFinder(object):



    #hash table
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr=[]

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        newarr=[]
        if len(self.arr)==0:
            self.arr=[num]
        id=-1
        for i in range(len(self.arr)):
            if num<self.arr[i]:
                id=i
                break
        if id==-1:
            self.arr.append(num)
        else:
            self.arr=self.arr[:id]+[num]+self.arr[id:]
        print self.arr

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.arr)%2:
            return self.arr[len(self.arr)/2]
        else:
            return (self.arr[len(self.arr)/2-1]+self.arr[len(self.arr)/2])/2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# print [1,2]+[3]

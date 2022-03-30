class MedianFinder(object):

    def __init__(self):
        self.numArr=[]
        self.mideanPtr=-1


    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        for i in range(len(self.numArr)):
            if num<self.numArr[i]:
                self.numArr=self.numArr[:i+1]
                left=self.numArr[i+1:]
                self.numArr.append(num)
                self.numArr.extend(left)


    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.numArr)==0:
            return -1
        if len(self.numArr)%2==0:
            return float(self.numArr[len(self.numArr)/2]+self.numArr[len(self.numArr)/2+1])/2
        else:
            return not self.numArr[len(self.numArr)/2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
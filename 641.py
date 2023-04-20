class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.list = [0] * (k + 1)
        self.head = 0
        self.tail = 0
        self.len = k + 1

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False

        self.head = (self.head - 1) % self.len
        self.list[self.head] = value
        return True

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.list[self.tail] = value
        self.tail = (self.tail + 1) % self.len
        return True

    def deleteFront(self):
        """kl;]
        \
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.len
        return True

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.tail = (self.tail - 1) % self.len
        return True

    def getFront(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return False
        return self.list[self.head]

    def getRear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return False
        return self.list[(self.tail - 1) % self.len]

    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.head == self.tail:
            return True
        return False

    def isFull(self):
        """
        :rtype: bool
        """
        if self.head == (self.tail + 1) % self.len:
            return True
        return False

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()



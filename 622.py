class MyCircularQueue(object):

        def __init__(self, k):
            """
            :type k: int
            """
            self.circle=[0]*(k+1)
            self.head=0
            self.tail=0
            self.quelen=k+1

        def enQueue(self, value):
            """
            :type value: int
            :rtype: bool
            """
            if self.isFull():
                return False

            self.tail=(1+self.tail)%self.quelen
            self.circle[self.tail]=value
            return True

        def deQueue(self):
            """
            :rtype: bool
            """
            if self.isEmpty():
                return False
            self.head=(1+self.head)%self.quelen
            # self.circle[self.head]
            return True


        def Front(self):
            """
            :rtype: int
            """
            if self.isEmpty():
                return -1
            return self.circle[(1+self.head)%self.quelen]

        def Rear(self):
            """
            :rtype: int
            """
            if self.isEmpty():
                return -1

            return self.circle[self.tail]
        def isEmpty(self):
            """
            :rtype: bool
            """
            return self.head==self.tail

        def isFull(self):
            """
            :rtype: bool
            """
            return (self.tail+1)%self.quelen==self.head




    # Your MyCircularQueue object will be instantiated and called as such:
    # obj = MyCircularQueue(k)
    # param_1 = obj.enQueue(value)
    # param_2 = obj.deQueue()
    # param_3 = obj.Front()
    # param_4 = obj.Rear()
    # param_5 = obj.isEmpty()
    # param_6 = obj.isFull()

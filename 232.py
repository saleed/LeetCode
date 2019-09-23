class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.st1=[]
        self.st2=[]

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.st1.append(x)
        if len(self.st2)==0:
            while len(self.st1)>0:
                ele=self.st1.pop()
                self.st2.append(ele)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.st2)==0:
            while len(self.st1)>0:
                ele=self.st1.pop()
                self.st2.append(ele)
        if len(self.st2)>0:
            return self.st2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.st2)==0:
            while len(self.st1)>0:
                ele=self.st1.pop()
                self.st2.append(ele)
        if len(self.st2) > 0:
            ele =self.st2.pop()
            self.st2.append(ele)
            return ele


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.st1)==0 and len(self.st2)==0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
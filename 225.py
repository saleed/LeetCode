import Queue
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que=Queue.Queue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.que.put(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        que=self.que
        newque=Queue.Queue()
        ret=que.get()
        while not que.empty():
            newque.put(ret)
            ret=que.get()
        self.que=newque
        return ret


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        que=self.que
        newque=Queue.Queue()
        ret=que.get()
        while not que.empty():
            newque.put(ret)
            ret=que.get()
        newque.put(ret)
        self.que=newque
        return ret



    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.que.empty()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


que=Queue.Queue()
print not que.empty()

a=MyStack()
a.push(1)
a.push(2)
print a.top()
print a.pop()
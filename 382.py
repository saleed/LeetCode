# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head=head
        self.curptr=head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        if self.head==None:
            return None
        if self.curptr==None:
            self.curptr=self.head
        ret= self.curptr.val
        self.curptr=self.curptr.next
        return ret




# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
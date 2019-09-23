# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #不做结构变换，直接按照加法规则处理


        p=l1
        q=l2
        c=0
        res=ListNode(0)
        res.next=None



        while p!=None or q!=None:
            if p!=None:
                add1=djfkdsjfsdkfsdk

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        id=[0]*len(lists)
        while True:
            flag=0
            maxval=-float("inf")
            sel=-1
            for i in range(len(lists)):
                if id[i]==len(list[i]):
                    continue
                else:
                    if list[i][]


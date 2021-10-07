# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ptr_list=[]
        newhead=ListNode(0)
        r=newhead
        for p in lists:
            ptr_list.append(p)

        while True:
            flag=0
            for p in ptr_list:
                if p!=None:
                    flag=1
            if flag==0:
                return newhead.next
            minval=float("inf")
            idx=0
            for i in range(len(ptr_list)):
                if ptr_list[i]==None:
                    continue
                if ptr_list[i].val<minval:
                    minval=ptr_list[i].val
                    idx=i
            node=ListNode(minval)
            ptr_list[idx]=ptr_list[idx].next
            r.next=node
            r=r.next

    def heapfiy(self,ptr_list):
        




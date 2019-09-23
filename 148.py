# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head

        return self.mergeSort(head)



    def mergeSort(self,head):
        if head==None:
            return None
        print "##",head.val
        if head.next==None:
            return head
        head1=head2=head
        if head.next.next==None: #be careful for this
            head1=head
            head2=head.next
            head.next=None
        else:
            while head2 and head2.next:
                head1=head1.next
                head2=head2.next.next
            head2=head1.next
            head1.next=None
            head1=head
        self.printlist(head1)
        self.printlist(head2)
        sorted1=self.mergeSort(head1)
        sorted2=self.mergeSort(head2)
        # self.printlist(sorted1)
        # self.printlist(sorted2)
        return self.merge(sorted1,sorted2)




    def merge(self,head1,head2):
        newhead=ListNode(0)
        p=newhead
        while head1!=None and head2!=None:
            if head1.val<head2.val:
                p.next=head1
                head1=head1.next
            else:
                p.next=head2
                head2=head2.next
            p=p.next
        if head1!=None:
            p.next=head1
        elif head2!=None:
            p.next=head2
        return newhead.next

    def printlist(self,head):
        res=[]
        if head==None:
            return res
        p=head
        while p!=None:
            res.append(p.val)
            p=p.next
        print res


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodeval=[]
        p=head
        while p!=None:
            nodeval.append(p.val)
            p=p.next

        p1=0
        p2=len(nodeval)-1
        while p1<p2:
            if nodeval[p1]!=nodeval[p2]:
                return False

            p1+=1
            p2-=1
        return True


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        st=[]
        count=0
        p=head
        while p!=None:
            st.append(p)
            count+=1
            p=p.next
        c=0
        p=head
        while c<count/2:
            q=p.next
            p.next=st.pop()
            p=p.next
            if p==q:
                break
            p.next=q
            p=q
            c+=1
        p.next=None
        return head


st=[1,2]
print(st.pop())
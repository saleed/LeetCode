class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        dummyhead=ListNode(0)
        cnt=0
        dummyhead.next=head
        p=dummyhead
        while cnt<left-1 and p!=None:
            p=p.next
            cnt+=1
        leftp=p
        while cnt<right+1 and p!=None:
            p=p.next
            cnt+=1
        rightp=p
        self.reverse(leftp,rightp)
        return dummyhead.next




    def reverse(self,head,tail):
        if head==None:
            return
        p=head.next
        q=p.next if p!=None else None
        r=q.next if q!=None else None
        p.next=None ####一定要注意头结点删除
        while q!=None and q!=tail:
            q.next=p
            p=q
            q=r
            r=r.next if r!=None else None

        if tail!=None:
            if head.next!=None:
                head.next.next=tail
        head.next=p

        return


a=ListNode(1)
p=a
p.next=ListNode(2)
p=p.next
p.next=ListNode(3)
p=p.next
p.next=ListNode(9)
p=p.next
p.next=ListNode(4)
p=p.next
p.next=ListNode(5)
p=p.next
p=a
while p!=None:
    print(p.val)
    p=p.next

So=Solution()
print(So.reverseBetween(a,2,4))
p=a
while p!=None:
    print(p.val)
    p=p.next
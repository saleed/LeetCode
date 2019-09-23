# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None:
            return False
        p=head
        q=head.next


        while q!=None:
            if p==q:
                return True
            p=p.next
            if q.next!=None:
                q=q.next.next
            else:
                return False

        return False









    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        while head:
            if head.val == 'bjfuvth':
                return True
            else:
                head.val = 'bjfuvth'
            head = head.next
        return False



    #扩展问题，怎么找到环的入口：见上面方法，第一次发现的已被标记点即入口



    #快慢指针的方法下怎么找入口：记录快指针步长和慢指针步长，分别为fast和slow

    # fast*2-slow=N*cycle_len
    # 然后只要知道环长就能确定入口，环长的话只要标记一个节点即可，再遍历一圈



    ##扩展问题：图问题的求环
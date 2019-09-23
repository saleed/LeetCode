
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random



#要点：
#1.新建立一条链表一定是使用头插法或者尾插法：两种方法都需要插入点的前一个节点指针！！！！！！
#2.每次新创建一个节点后，需要额外处理random指针，random指针只要记录下random指针的指向关系即刻
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head==None:
            return None

        dict={}

        p=head

        dummy=Node(0,None,None)
        q=dummy

        while p:
            if p in dict.keys():
                q.next=dict[p]
            else:
                q.next=Node(p.val)
                dict[p] = q
            q=q.next
            if p.random:
                if p.random in dict.keys():
                    q.random=dict[p.random]
                else:
                    q.random=Node(p.random.val)
                    dict[p.random]=q.random
            p=p.next
        return dummy.next








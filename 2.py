# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#method1: convert each given single list to a int and then do addition,then convert to a result linklist


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.num2reverselist(self.reverse2Number(l1)+self.reverse2Number(l2))

    def reverse2Number(self,l):
        t=1
        sum=0
        for i in l:
            sum+=i*t
            t*=10
        return sum

    def num2reverselist(self,n):
        a=[]
        while(n):
            a.append(n%10)
            n/=10
        return a




#########################################################################################
#method2: reverse each given linklist and do bit addtion with a carry
    def addTwoNumbers2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #first reversed list1 and list2
        rl1,len1=self.reverse2Number(l1)
        rl2,len2=self.reverse2Number(l2)

        #\








    def reverseLinkList(self,head):
        if head==None:
            return head,0
        if head.next==None:
            return head,1
        l1=head
        l2=head.next
        l3=head.next.next
        l=2
        while l3!=None:
            l+=1
            l2.next=l1
            l1=l2
            l2=l3
            l3=l3.next
        head.next=None
        l2.next=l1
        return l2,l





a=[1,2,3]
b=Solution()
print reversed(a)

print b.reverse2Number(a)
print b.num2reverselist(321)

a1=[2,4,3]
a2=[5,6,4]
print b.addTwoNumbers(a1,a2)


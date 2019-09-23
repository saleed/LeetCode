import gc

class BT:
    def __init__(self,val=-1):
        self.left=None
        self.right=None
        self.val=val



import copy




t=BT()
print(t.val)
t.left=BT(2)
p=t.left
# del p
# print(p)
# gc.collect()
# print(p)
# print(id(p))
print(t.left)
print(t.left.val)
# t.left=None
# print(t.left)

a=[1,2,3,4]
b=copy.copy(a)

print(id(a))
print(id(b))

import  sys
line=sys.stdin.readline()
listline=list(map(int,line.split()))
print(listline)



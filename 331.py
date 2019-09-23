class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        pre=preorder.split(",")
        print pre
        if len(pre)==0:
            return False
        ptr=1
        child=[pre[0]]
        while len(child)>0:
            newchild=[]
            for i in child:
                if i!='#':
                    if ptr+2>len(pre):
                        return False
                    newchild.extend(pre[ptr:ptr+2])
                    ptr+=2
            child=newchild
        if ptr!=len(pre):
            return False
        else:
            return True

    def isValidSerialization2(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        # remember how many empty slots we have
        # non-null nodes occupy one slot but create two new slots
        # null nodes occupy one slot

        p = preorder.split(',')

        # initially we have one empty slot to put the root in it
        slot = 1
        for node in p:

            # no empty slot to put the current node
            if slot == 0:
                return False

            # a null node?
            if node == '#':
                # ocuppy slot
                slot -= 1
            else:
                # create new slot
                slot += 1

        # we don't allow empty slots at the end
        return slot == 0


a=Solution()
Input= "9,3,4,#,#,1,#,#,2,#,6,#,#"
print a.isValidSerialization(Input)
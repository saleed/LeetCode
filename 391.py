class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        corner=set()
        recset=set()
        for rec in rectangles:
            if rec in recset:
                continue
            else:
                recset.add(rec)
            if (rec[0],rec[1]) not in corner:
                corner.add((rec[0],rec[1]))
            else:
                corner.remove((rec[0],rec[1]))
            if (rec[0],rec[3]) not in corner:
                corner.add((rec[0],rec[3]))
            else:
                corner.remove((rec[0],rec[3]))
            if (rec[2],rec[1]) not in corner:
                corner.add((rec[2],rec[1]))
            else:
                corner.remove((rec[2],rec[1]))
            if (rec[2],rec[3]) not in corner:
                corner.add(rec[2],rec[3])
            else:
                corner.remove((rec[2],rec[3]))
        return len(corner)==4









    def spotInRectange(self,x,y,ldx,ldy,urx,ury):
        if (x==ldx or x==urx) and (y==ldy or y==ury)
            return True
        return False






#try to think another question:
#given  server rectangle with different width and height, how to determine if they can combine to a big rectangle?
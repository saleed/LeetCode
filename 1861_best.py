class Solution(object):
    def rotateTheBox(self, box):
        """
        :type box: List[List[str]]
        :rtype: List[List[str]]
        """

        barrier=[float("inf")]*len(box)
        stone=
        for i in range(len(box)):
            for j in range(len(box[0])):
                if box[i][j]=="*":
                    barrier[i]=min(barrier[i],j)
                if box[i][j]=="#":
                    b


        ret=[["." for _ in range(len(box))] for _ in range(len(box[0]))]






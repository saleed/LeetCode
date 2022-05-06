class Solution(object):
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """

        num=[str(i) for i in range(1,n+1)]

        while len(num)>1:
            p=0
            q=len(num)-1
            newnum=[]
            while p<q:
                newnum.append("("+num[p]+","+num[q]+")")
                p+=1
                q-=1
            num=newnum
        return num[0]

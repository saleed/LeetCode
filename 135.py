class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if len(ratings)==0:
            return 0
        return self.solve(ratings)


        #首先考虑可行解，不考虑最优解
    def avabiableSolve(self,ratings):
        candys=[1]*len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1] and candys[i]<=candys[i-1]:
                candys[i]=candys[i-1]+1
            elif ratings[i]<ratings[i-1] and candys[i]>=candys[i-1]:
                candys[i-1]=candys[i]+1



    def solve(self,rating):
        candys=[1]*len(rating)
        for i in range(1,len(rating)):
            if rating[i]>rating[i-1] and candys[i]<=candys[i-1]:
                candys[i]=candys[i-1]+1
        for j in list(reversed(range(len(rating)-1))):
            if rating[j]>rating[j+1] and candys[j]<=candys[j+1]:
                candys[j]=candys[j+1]+1
        return sum(candys)



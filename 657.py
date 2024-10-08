class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x=0
        y=0
        for v in moves:
            if v=="U":
                y+=1
            elif v=="D":
                y-=1
            elif v=="L":
                x-=1
            else:
                x+=1
        return x==0 and y==0
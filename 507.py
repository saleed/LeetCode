class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """

        sq=int(math.sqrt(num))
        res=0
        for i in range(2,sq):
            if num%i==0:
                res+=i
                res+=num/i
        return res+1==num

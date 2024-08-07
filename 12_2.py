class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        cdict=["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
        vdict=[1,4,5,9,10,40,50,90,100,400,500,900,1000]

        """
        1.能表示的数的上限->MMM 3000
        2.是否能表示1到上限的任何一个数字，为什么
        """

        res=""
        while num>0:
            for i in range(len(vdict))[::-1]:
                if vdict[i]<=num:
                    num-=vdict[i]
                    res+=cdict[i]
                    break
        return res
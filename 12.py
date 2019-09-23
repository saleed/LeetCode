class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # dict={
        #     'I':1,'IV':4,'V':5,'IX':9,'X': 10,'XL':40,'L': 50,'C': 100,'CD':400,'D':500,'CM':900,'M':1000}
        #
        res=""
        charr=['I','IV','V','IX','X','XL','L','C','CD','D','CM','M']
        vararr=[1,4,5,9, 10,40,50, 100,400,500,900,1000]
        # for key,val in dict.items():
        #     charr.append(key)
        #     vararr.append(val)
        # print(charr,vararr)
        while num:
            # print(num)
            for i in list(reversed(range(len(vararr)))):
                if num-vararr[i]>=0:
                    res+=charr[i]
                    num=num-vararr[i]
                    break
        return res

a=Solution()
print(a.intToRoman(9))




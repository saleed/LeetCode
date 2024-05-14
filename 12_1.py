class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        cdict=["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
        vdict=[1,4,5,9,10,40,50,90,100,400,500,900,1000]

        res=""
        while num>0:
            for i in range(len(cdict))[::-1]:
                # print("11", i, vdict[i])
                if num>=vdict[i]:
                #     print("XXX",i,vdict[i])
                    res+=cdict[i]
                    # print(res)
                    num-=vdict[i]
                    # print(num)
                    break
        return res

cdict=["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
vdict=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
print(len(cdict))
print(len(vdict))

s=Solution()
print(s.intToRoman(20))
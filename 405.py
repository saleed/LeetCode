class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        return self.solove2(num)


    def solove1(self,num):
        if num==0:
            return "0"
        dict={0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"a",11:"b",12:"c",13:"d",14:"e",15:"f"}

        if num<0:
            num+=pow(2,32)
        res=""
        while num:
            left=num%16
            res=dict[left]+res
            num=int(num/16)
        return res

    def solove2(self,num):
        res=""
        if num==0:
            return "0"
        if num<0:
            num+=pow(2,32)
        while num:
            left=num%16
            if left<10:
                res=str(left)+res
            else:
                res=chr(left-10+ord('a'))+res
            num=num/16
        return res










a=Solution()
print(a.toHex(-1))
print(a.toHex(16))


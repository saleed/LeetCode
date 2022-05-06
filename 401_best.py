class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """

        res=[]
        self.dfs(0,0,turnedOn,res)
        # print(res)
        strres=[]
        for i in res:
            t=self.decode(i)
            if t!=-1:
                strres.append(t)
                # print(bin(i),t)

        return strres

    def dfs(self,bitd,i,left,res):
        if left==0:
            # print(bin(bitd))
            res.append(bitd)
            return
        elif i<10:
            self.dfs(bitd,i+1,left,res)
            bitd=bitd|(1<<(10-i-1))
            self.dfs(bitd,i+1,left-1,res)

    def decode(self,bitd):

        hour=bitd>>6
        minute=bitd&((1<<6)-1)

        if (hour>=12 or minute>=60):
            return -1

        print(bin(bitd),hour,minute)
        strhour=str(hour)
        strminute=str(minute) if minute>=10 else "0"+str(minute)

        return str(strhour)+":"+str(strminute)


s=Solution()
print(s.readBinaryWatch(9))
print(bin((1<<6)-1))
print(0000111111)
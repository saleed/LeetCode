class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        leds=[0]*10
        res=[]
        self.dfs(num,leds,res,0)
        time=self.getTime(res)
        # print res
        return time



    def dfs(self,nums,led,res,id):
        if nums==0:
            res.append(led[:])
            return
        if nums>len(led)-id:
            return
        self.dfs(nums,led,res,id+1)
        led[id]=1
        self.dfs(nums-1,led,res,id+1)
        led[id]=0
        return

    def getTime(self,leds):
        T=[]
        for led in leds:
            hour=0
            miniute=0
            if led[0]==1:
                hour+=8
            if led[1]==1:
                hour+=4
            if led[2]==1:
                hour+=2
            if led[3]==1:
                hour+=1
            if led[4]==1:
                miniute+=32
            if led[5] == 1:
                miniute += 16
            if led[6] == 1:
                miniute += 8
            if led[7] == 1:
                miniute += 4
            if led[8] == 1:
                miniute += 2
            if led[9] == 1:
                miniute += 1
            # print hour,miniute
            if hour<12 and miniute<60:  ####notice here

                H=str(hour)
                if miniute<10:
                    M='0'+str(miniute)
                else:
                    M=str(miniute)
                T.append(H+":"+M)
        return T



a=Solution()
print a.readBinaryWatch(1)

["0:03","0:05","0:06","0:09","0:10","0:12","0:17","0:18","0:20","0:24","0:33","0:34","0:36","0:40","0:48","1:01","1:02","1:04","1:08","1:16","1:32","2:01","2:02","2:04","2:08","2:16","2:32","3:00","4:01","4:02","4:04","4:08","4:16","4:32","5:00","6:00","8:01","8:02","8:04","8:08","8:16","8:32","9:00","10:00","12:00"]
["0:03","0:05","0:06","0:09","0:10","0:12","0:17","0:18","0:20","0:24","0:33","0:34","0:36","0:40","0:48","1:01","1:02","1:04","1:08","1:16","1:32","2:01","2:02","2:04","2:08","2:16","2:32","3:00","4:01","4:02","4:04","4:08","4:16","4:32","5:00","6:00","8:01","8:02","8:04","8:08","8:16","8:32","9:00","10:00"]
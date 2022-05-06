class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt=n
        step=1
        start=0
        k=0

        while cnt>1:
            if k%2==0:
                start=start+step
            else:
                if cnt%2==0:
                    start=start+step
            cnt/=2
            k+=1
            step*=2
        return start




    def simulate(self,n):

        #time limit exceed

        num=n+1
        d=2
        vis=set()
        while num>1:
            flag=1
            start=0
            if flag==1:
                for i in range(1,n+1):
                    if i not in vis:
                        start=i
            else:
                for i in range(1,n+1)[::-1]:
                    if i not in vis:
                        start=i
            i=0
            while start+flag*d*i>=0 and start+flag*d<=n:
                vis.add(start+flag*d*i)
                i+=1
                num-=1
            flag*=-1
            d=d*2
        for i in range(1,n+1):
            if i not in vis:
                return i



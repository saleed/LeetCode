class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        explist=self.processExp(expression)
        print(explist)
        gcd=explist[0][1]
        for v in explist:
            gcd=(gcd*v[1])/self.gcd(gcd,v[1])

        headsum=0
        for v in explist:
            headsum+=v[0]*gcd/v[1]
        print(headsum)
        if headsum==0:
            return "0/1"
        newgcd=self.gcd(abs(headsum),abs(gcd))

        return str(headsum/newgcd)+"/"+str(gcd/newgcd)


    def processExp(self,expression):
        expression=expression+"+"
        i=0
        res=[]
        pre=""
        while i<len(expression):
            if expression[i]=="+" or expression[i]=="-":
                if pre!="":
                    if "/" in pre:
                        pre=pre.split("/")

                        res.append((int(pre[0]),int(pre[1])))
                    else:
                        res.append([0,int(pre)])
                pre=""
            pre+=expression[i]
            i+=1
        return res












    def gcd(self,a,b):
        if a<b:
            a,b=b,a
        while a%b:
            tmp=b
            b=a%b
            a=tmp
        return b



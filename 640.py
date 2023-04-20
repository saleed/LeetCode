class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """

        startflag=1
        xcoef=0
        bcoef=0
        i=0
        flag=startflag
        while i<len(equation):
            if equation[i]=="+":
                flag=startflag
                i+=1
            elif equation[i]=="-":
                flag=-startflag
                i+=1
            elif equation[i]=="x":
                xcoef+=flag
                i+=1
            elif equation[i].isdigit():
                start=i
                while i<len(equation) and equation[i].isdigit():
                    i+=1
                if i==len(equation):
                    bcoef+=(flag*int(equation[start:i]))
                else:
                    if equation[i]=="x":
                        xcoef+=(flag*int(equation[start:i]))
                        # print(xcoef, equation[start:i])
                        i+=1
                    else:
                        bcoef+=(flag*int(equation[start:i]))

            elif equation[i]=="=":
                startflag=-1 ## 移动到左边
                flag=-1
                i+=1


            print(i,xcoef,bcoef,flag)
        if xcoef == 0 and bcoef!=0:###无解的
            return "No solutions"
        elif xcoef==0 and bcoef==0:##无限解
            return  "Infinite solutions"
        if  abs(bcoef)%abs(xcoef)==0: ##
            bcoef=int(bcoef/xcoef)
            xcoef=1

        if xcoef<0:
            xcoef=-xcoef
            bcoef=-bcoef

        if xcoef==1:
            return "x="+str(-bcoef)
        else:
            return str(xcoef)+"x="+str(-bcoef)
        # equation = "x+5-3+x=6+x-2"


equation ="2x+3x-6x=x+2"
ss=Solution()
print(ss.solveEquation(equation))







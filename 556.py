class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        n=int(n)
        listn=[]
        while n:
            listn.append(n%10)
            n=int(n/10)
        listn=listn[::-1]

        for i in range(len(listn))[::-1]:
            if i==0 or(i>0 and listn[i]<=listn[i-1]):
                continue
            else:
                id=i
                print(listn)
                for j in range(len(listn))[::-1]:
                    if listn[j]>listn[i-1]:
                        print("XX",listn[j],listn[i-1])
                        id=j
                        break
                print(id)
                listn[id],listn[i-1]=listn[i-1],listn[id]
                p=i
                q=len(listn)-1
                print(listn)
                while p<q:
                    listn[p],listn[q]=listn[q],listn[p]
                    p+=1
                    q-=1
                res = 0
                print(listn)
                for v in listn:
                    res = res * 10 + v
                return res
        return -1



test=101
ss=Solution()
print(ss.nextGreaterElement(test))
import math
print(math.pow(2,31)-1)
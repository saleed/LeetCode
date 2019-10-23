class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people=sorted(people,key=lambda x:(x[0],-x[1]))

        #发现一个大问题：python 的sorted怎么自定义比较函数，现在只直到怎么使用匿名函数，匿名函数可以多字段
        print(people)
        res=[]
        while len(people)>0:
            tail=people[-1]
            # print(res[:tail[1]],[tail],res[tail[1]+1:])
            res=res[:tail[1]]+[tail]+res[tail[1]:]
            people.pop()

        return res



def cmp(self,x,y):
    if x[0] > y[0] or (x[0] == y[0] and x[1] < y[1]):
        return 1
    else:
        return -1



a=Solution()
people=[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(a.reconstructQueue(people))
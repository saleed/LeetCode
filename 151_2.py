class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.solve(s)






    def solve(self,s):
        if len(s)==0:
            return ""
        slist=s.split(" ")
        newlist=[]
        for i in slist:
            if i!='':
                newlist.append(i)
        slist=newlist
        print(slist)
        slist=list(reversed(slist))
        ret=" ".join(slist)
        return ret

    def siglebitSolve(self,s):
        self.reverse(s,0,len(s)-1)
        start=0
        flag=0
        s.lstrip(" ")
        s.rstrip(" ")
        for i in range(len(s)):
            if flag==0 and s[i]!=" ":
                flag=1
                start=i
            elif flag==1 and s[i]==" ":
                self.reverse(start,i-1)
                flag=0
        self.reverse(s,start,len(s)-1)
        print(s)



    def reverse(self,s,i,j):
        p=i
        q=j
        while p<q:
            tmp = s[i]
            s[i] = s[j]  ####error python中str类型不能更改值: 'str' object does not support item assignment
            s[j] = tmp
            p+=1
            q-=1

a=Solution()

test="a good example"
print(a.reverseWords(test))
test="  hello world!  "
print(a.reverseWords(test))
# print("".join(list(reversed(test))))

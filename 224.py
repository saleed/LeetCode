class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if len(s)==0:
        #     return 0
        # if s[0]=='(' or s[0]==')':
        #     return self.calculate(s[1:])
        s=self.strProcess(s)
        cur=s[0]
        i=1
        while i<len(s):
            if s[i] == '-':
                cur = cur-s[i+1]
            if s[i] == '+':
                cur = cur+s[i+1]
            i+=2
        return cur

    #
    # def strProcess(self,s):
    #     print s
    #     if len(s) == 0:
    #         return 0
    #     if s[0] != '-' and s[0] != '+':
    #         cur = ord(s[0]) - ord('0')
    #         if len(s) > 1 and s[1] == '-':
    #             cur= cur - self.strProcess(s[2:])
    #         elif len(s) > 1 and s[1] == '+':
    #             cur =cur + self.strProcess(s[2:])
    #         print cur
    #         return cur

    def strProcess(self,s):
        s = s.replace('(', '')
        s = s.replace(')', '')
        s = s.replace(' ', '')
        print(s)
        ret=[]
        p=0
        while p<len(s):
            start=p
            while  p<len(s) and s[p]!='+' and  s[p]!='-' :
                p+=1
            ret.append(int(s[start:p]))
            if p>=len(s):
                break
            ret.append(s[p])
            p+=1
        return ret





s="(1+(42323+5+2)-3)+(6+8)"
a=Solution()
# print s.replace('(',"2323")  #WARNING: the replace function ret the repalced string rather than do replacing opration in the string itself
print(s)
print( a.calculate(s))
print (a.strProcess(s))
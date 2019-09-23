class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        print s
        if s=="":
            return ""
        if s[0].isalpha():
            return s[0]+self.decodeString(s[1:])
        if s[0].isdigit():
            ptr=1
            while ptr<len(s) and s[ptr].isdigit():
                ptr+=1
            # return int(s[:ptr])*self.decodeString(s[ptr:])
            repeat=int(s[:ptr])
            strstart=ptr+1
            stack=['[']
            while len(stack)>0:
                ptr+=1
                if s[ptr]=='[':
                    stack.append('[')
                elif s[ptr]==']':
                    stack.pop()
            return repeat*(self.decodeString(s[strstart:ptr]))+self.decodeString(s[ptr+1:])

s = "3[a]2[bc]"
a=Solution()
print a.decodeString(s)

print 3*"aaa"
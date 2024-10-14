import copy

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """


        return self.dfs(s)


    def dfs(self,s):
        res=0
        flag=1
        i=0
        print(s)
        while i<len(s):
            if s[i]==" ":
                continue
            elif s[i]=="+":
                flag=1
                i+=1
            elif s[i]=="-":
                flag=-1
                i+=1
            elif s[i]=="(":
                st=["("]
                p=i+1
                while len(st)!=0:
                    # print(st)
                    if s[p]=="(":
                        st.append("(")
                    elif s[p]==")":
                        st.pop()
                    p+=1
                # print(i,p)
                res+=flag*self.dfs(s[i+1:p-1])
                i=p
            else:
                digit=0
                while i<len(s) and s[i].isdigit():
                    digit=digit*10+int(s[i])
                    i+=1
                res+=flag*digit
        # print(s,res)
        return res


##超时

s=Solution()
test="2147483647"
print(test[0:5])
print(s.calculate(test))
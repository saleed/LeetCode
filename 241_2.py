class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """

        input=list(input)
        return self.dfs(input)


    def dfs(self,input):
        print(input)
        res = []
        op = input[1]
        ld = int(input[0])
        if len(input)==3:
            if op=='-':
                return [ld-int(input[2])]
            elif op == '+':
                return [ld +int(input[2])]
            elif op == '*':
                return [ld *int(input[2])]
        else:
            if op=='-':
                nextres=self.dfs(input[2:])
                for i in nextres:
                    res.append(ld-i)
                ld-=int(input[2])
                newinput=[ld]+input[3:]
                res.extend(self.dfs(newinput))
            if op=='+':
                nextres=self.dfs(input[2:])
                for i in nextres:
                    res.append(ld+i)
                ld+=int(input[2])
                newinput=[ld]+input[3:]
                res.extend(self.dfs(newinput))
            if op=='*':
                nextres=self.dfs(input[2:])
                for i in nextres:
                    res.append(ld*i)
                ld*=int(input[2])
                newinput=[ld]+input[3:]
                res.extend(self.dfs(newinput))
        return res
a=Solution()
s= "2*3-4*5"
print(a.diffWaysToCompute(s))
# s=[1,2,3]
# print([5]+s)
# print(list(s))
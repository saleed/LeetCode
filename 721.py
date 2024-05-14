class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """

        res=[]
        for v in accounts:
            name=v[0]
            email=list(set(v[1:]))
            flag=0
            for i in range(len(res)):
                if len(set(res[i][1:]).intersection(set(email)))>0:
                    newres=list(set(res[i][1:]+email))
                    newres.sort()
                    res[i]=[name]+newres
                    flag=1
            if flag==0:
                email.sort()
                res.append([name]+email)
            print(res)
        return res




    def accountsMerge2(self, accounts):




a=[1,2,3,4]
b=[2,3]
print(set(a).intersection(b))

accounts =[["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]

a=Solution()
print(a.accountsMerge(accounts))




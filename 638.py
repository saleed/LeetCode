class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        for i in range(len(special)):
            sumprice=0
            for j in range(len(special[i])-1):
                sumprice+=price[j]*special[i][j]
            if sumprice<special[i][-1]:
                special[i]=[]

        res=[float("inf")]
        self.dfs(price,special,needs,0,0,res)


    def dfs(self,price,specical,needs,i,tmp,res):
        if i==len(specical):
            res[0]=min(res[0],tmp+sum(needs[i]*price[i] for i in range(len(needs))))
            return
        if len(specical[i])==0:
            self.dfs(price,specical,needs,i+1,tmp,res)
            return
        i=0
        while True:
            nxtneed=[]
            flag=0
            for j in range(len(needs)):
                print(j,len(needs))
                if needs[j]-specical[i][j]<0:
                    flag=1
                    break
                nxtneed.append(needs[j]-specical[i][j])
            if flag:
                return

            tmpcost=tmp+specical[i][-1]
            # newtmpKey=tuple(newtmp)
            # tmpKey=tuple(tmp)
            # if newtmpKey not in res:
            #     res[newtmpKey]=res[tmpKey]+i*specical[i][-1]
            # else:
            #     res[newtmpKey]=min(res[newtmpKey],res[tmpKey]+i*specical[i][-1])

            self.dfs(price,specical,nxtneed,i+1,tmpcost,res)
            i+=1



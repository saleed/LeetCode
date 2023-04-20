eclass Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """

        pairlist = []
        strnum = list(str(num))
        for i in range(len(strnum)):
            pairlist.append([strnum[i], i])

        pairlist = sorted(pairlist,key=lambda x:(x[0],-x[1]),reverse=True)
        print(pairlist)
        for i in range(len(strnum)):
            if pairlist[i][0]!=strnum[i]:
                strnum[i], strnum[pairlist[i][1]] = strnum[pairlist[i][1]], strnum[i]
                break
            else:
                strnum[i], strnum[pairlist[i][1]] = strnum[pairlist[i][1]], strnum[i]

        return int("".join(strnum))
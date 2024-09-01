class Solution(object):
    def flipLights(self, n, presses):
        """
        :type n: int
        :type presses: int
        :rtype: int
        """

        resset = set()

        sset = set()
        tmpstate = [0, 0, 0, 0]

        presses=min(presses,4) ###优化点2 总共4种操作，4次操作便可以覆盖全部情况


        self.dfs(sset, presses, tmpstate)
        print(sset)




        for v in sset:
            tmp = [0] * min(6,n)  ###优化点1，灯泡亮灭周期为6
            # print(v)
            if v[0]:
                for i in range(len(tmp)):
                    tmp[i] = 1 - tmp[i] if i % 2 == 1 else tmp[i]
            if v[1]:
                for i in range(len(tmp)):
                    tmp[i] = 1 - tmp[i] if i % 2 == 0 else tmp[i]
            if v[2]:
                for i in range(len(tmp)):
                    if 3 * i + 1 < len(tmp):
                        tmp[3*i] = 1 - tmp[3*i]
            print(v,tmp)
            resset.add(tuple(tmp))
        return len(resset)

    def dfs(self, stateset, i, tmpstate):
        if i == 0:
            self.simpfiyState(tmpstate, stateset)
        else:
            tmpstate[0] += 1
            self.dfs(stateset, i - 1, tmpstate)
            tmpstate[0] -= 1

            tmpstate[1] += 1
            self.dfs(stateset, i - 1, tmpstate)
            tmpstate[1] -= 1

            tmpstate[2] += 1
            self.dfs(stateset, i - 1, tmpstate)
            tmpstate[2] -= 1

            tmpstate[3] += 1
            self.dfs(stateset, i - 1, tmpstate)
            tmpstate[3] -= 1

    def simpfiyState(self, raw, stateset):
        tmpstate = raw[1:]
        tmpstate[0] += raw[0]
        tmpstate[1] += raw[0]
        tmpstate[0] %= 2
        tmpstate[1] %= 2
        tmpstate[2] %= 2

        stateset.add(tuple(tmpstate))

ss=Solution()
n=4
m=100
print(ss.flipLights(n,m))


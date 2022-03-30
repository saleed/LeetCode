class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        pairdict = {"0": "0", "1": "1", "8": "8", "6": "9", "9": "6"}
        if n == 1:
            return ["1", "0", "8"]
        res = []
        self.dfs(n, 0, pairdict, res, "")
        print(res)
        if n % 2 == 0:
            newres=[]
            for i in range(len(res)):
                if res[i].startwith("0"):
                    continue
                r = ""
                for v in res[i][::-1]:
                    r += pairdict[v]
                res[i] = res[i] + r
            return res
        else:
            newres = []
            for i in range(len(res)):
                if res[i].startwith("0"):
                    continue
                r = ""
                for v in res[i][::-1]:
                    r += pairdict[v]
                for j in range(["0", "1", "8"]):
                    newres.append(res[i] + j + v)
            return newres

    def dfs(self, n, i, dict, res, tmp):
        if i == n / 2:
            res.append(tmp[:])
            return
        for v in dict:
            tmp += v
            self.dfs(n, i + 1, dict, res, tmp)
            tmp = tmp[:-1]




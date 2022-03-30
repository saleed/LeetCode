class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ndic = {}
        sel = set()
        for v in nums:
            if v in ndic:
                ndic[v] += 1
            else:
                ndic[v] = 1
            sel.add(v)

        res = []

        self.dfs(ndic, [], res, sel)
        return res

    def dfs(self, ndict, tmp, res, left):
        print(tmp, ndict)
        if len(left) == 0:
            res.append(tmp[:])
            return

        v = left.pop()
        # print(v)
        for i in range(ndict[v] + 1):
            tmp.extend([v] * i)
            self.dfs(ndict, tmp, res, left)
            tmp = tmp[:len(tmp) - i]

        left.add(v)




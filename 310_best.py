class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1: return [0]
        adjMat = {}
        for v in edges:
            if v[0] in adjMat:
                adjMat[v[0]].append(v[1])
            else:
                adjMat[v[0]] = [v[1]]

            if v[1] in adjMat:
                adjMat[v[1]].append(v[0])
            else:
                adjMat[v[1]] = [v[0]]

        leaves = [i for i in range(n) if len(adjMat[i]) == 1]
        while n > 2:
            newleaves = []
            for i in leaves:
                j = adjMat[i].pop()
                adjMat[j].remove(i)
                if len(adjMat[j]) == 1:
                    newleaves.append(j)
            n -= len(leaves)
            leaves = newleaves

        return leaves

class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash={}
        for v in nums:
            minv=0
            if v-1 in hash:
                minv=float("inf")
                for j in range(len(hash[v-1])):
                    if hash[v-1][j]<minv:
                        minv=hash[v-1][j]
                hash[v-1].remove(minv)
                if len(hash[v-1])==0:
                    del hash[v-1]

            if v in hash:
                hash[v].append(minv+1)
            else:
                hash[v]=[minv+1]

        for k in hash:
            for j in hash[k]:
                if j<3:
                    return False
        return True








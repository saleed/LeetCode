class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """

        if a!=b:
            return max(len(a),len(b))
        if a==b:
            return -1
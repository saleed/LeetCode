class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split(".")
        v2 = version2.split(".")

        for i in v1:
            self.clearZero(i)
        for j in v2:
            self.clearZero(j)
        m = 0
        print v1
        print v2
        if len(v1) < len(v2):
            v1.extend([0] * (len(v2) - len(v1)))
        else:
            v2.extend([0] * (len(v1) - len(v2)))
        for i in range(len(v1)):
            if int(v1[m]) < int(v2[m]):
                return -1
            elif int(v1[m]) > int(v2[m]):
                return 1

        return 0


def clearZero(self, version):
    if len(version) == 0:
        return version
    while len(version) > 0 and version[0] == "0":
        version = version[1:]
    if len(version) == 0:
        return "0"
    else:
        return version


a = "1.2"
b = "1.10"
print a > b
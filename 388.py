class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        depth=[]
        curlen=0
        ptr=0
        curstr=""
        maxlen=-float("inf")
        while ptr<len(input):
            if input[ptr]!='\n':
                curstr+=input[ptr]
            else:
                splitstr=curstr.split('.')
                if len(splitstr)==2 and splitstr[1]=='ext':
                    curdep=0
                    for i in depth:
                        maxlen=max(maxlen,len(curstr))
                curstr=""
                ptr+=1
                dep=0
                while ptr=='\t':
                    dep+=1
                    ptr+=1
                depth[]


def lengthLongestPath(input):
    maxlen = 0
    pathlen = {0: 0}
    for line in input.splitlines():
        print(line)
        name = line.lstrip('\t')
        depth = len(line) - len(name)
        if '.' in name:
            maxlen = max(maxlen, pathlen[depth] + len(name))
        else:
            pathlen[depth + 1] = pathlen[depth] + len(name) + 1
    return maxlen

input="dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
lengthLongestPath(input)
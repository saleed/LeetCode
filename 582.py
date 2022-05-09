class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """

        edge={}
        pidset=set()
        for i in range(len(pid)):
            if ppid[i] in edge:
                edge[ppid[i]].append(pid[i])
            else:
                edge[ppid[i]]=[pid[i]]
            pidset.add(pid[i])
            pidset.add(ppid[i])

        killset=set()

        while len(kill)>0:
            newtmpkill=[]
            for k in kill:
                killset.add(k)
                if k in edge:
                    for p in edge[k]:
                        if p not in killset:
                            newtmpkill.append(p)
                kill=newtmpkill
        res=[]
        for k in pidset:
            if k not in killset:
                res.append(k)
        return res







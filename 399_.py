class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """


        graph={}
        for i in range(len(equations)):
            v1=equations[i][0]
            v2=equations[i][1]
            if v1 not in graph:
                graph[v1]={}


            graph[v1][v2]=[1,values[i]]

            if v2 not in graph:
                graph[v2][v1]=[values[i],1]

        vis=set()
        que=[equations[0][0]]
        relation={}
        while len(que)>0:
            newque=[]
            for v in que:



        que=[]
        while len(que)>0:



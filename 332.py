import collections
class Solution(object):

    #?????????????????????????????????????????????????????????
    #exceeded time limit why?????????????????
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        dict={}
        if len(tickets)==0:
            return []
        for pair in tickets:
            if (pair[0] in dict.keys() and pair[1]<dict[pair[0]]) or pair[0] not in dict.keys():
                dict[pair[0]]=pair[1]

        start="JFK"
        res=[]
        while start in dict.keys():
            res.append(start)
            start=dict[start]
        res.append(start)
        return res

    def findItinerary2(self, tickets):
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]: #键和值拼接以后的大小d
            targets[a] += b,
        route = []
        print(targets)

        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)

        visit('JFK')
        return route[::-1]

Input=[["MUA", "LHZ"],["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]

print(sorted(Input))
a=Solution()
print(a.findItinerary2(Input))
# Input=[["JFK","SFO"]]
# print(a.findItinerary(Input))
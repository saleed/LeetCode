class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        return self.meiju(list1,list2)


    def meiju(self,list1,list2):

        indexsum=0
        while indexsum<len(list1)+len(list2)-1:
            res=[]
            for i in range(min(indexsum+1,len(list1))):
                if indexsum-i<len(list2) and list1[i]==list2[indexsum-i]:
                    res.append(list1[i])
            if len(res)>0:
                return res
            indexsum+=1
        return


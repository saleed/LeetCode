class LRUCache(object):
######################
##exceed time limit
#####链表的操作

    def __init__(self, capacity):
        """
        :type capacity: int
        """

        self.cap=capacity
        self.keyList=[]
        self.dataDict={}


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dataDict:
            for i in range(len(self.keyList)):
                if self.keyList[i]==key:
                    self.keyList[i], self.keyList[-1] = self.keyList[-1], self.keyList[i]
                    break
            return self.dataDict[key]
        return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        if key in self.dataDict:
            self.dataDict[key]=value
            for i in range(len(self.keyList)):
                if self.keyList[i]==key:
                    self.keyList[i],self.keyList[-1]=self.keyList[-1],self.keyList[i]
                    break
        else:
            self.dataDict[key]=value
            self.keyList.append(key)
            if len(self.keyList)>self.cap:
                del self.dataDict[self.keyList[0]]
                self.keyList=self.keyList[1:]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = {}
        self.ele = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.ele.append(val)
        if val in self.set.keys():
            self.set[val]+=1
            return False
        else:
            self.set[val]=1
            return True

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.set.keys():
            self.set[val]-=1
            if self.set[val]==0:
                del self.set[val]
            self.ele.remove(val)
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        print self.ele
        return self.ele[random.randint(0, len(self.ele) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


a=set()
print a.add(2)
a.add(3) # return Nothing
a.add(1)
a.add(4)
for i in a:
    print i
    break
a.remove(3)
for i in a:
    print i
    break


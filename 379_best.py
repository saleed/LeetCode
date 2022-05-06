class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        :type maxNumbers: int
        """
        self.phone=set()
        self.maxNumber=maxNumbers


    def get(self):
        """
        :rtype: int
        """
        for i in range(self.maxNumber):
            if i not in self.phone:
                self.phone.add(i)
                return i

        return -1

    def check(self, number):
        """
        :type number: int
        :rtype: bool
        """
        if number in self.phone:
            return  False
        else:
            return True

    def release(self, number):
        """
        :type number: int
        :rtype: None
        """
        if number in self.phone:
            self.phone.remove(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)



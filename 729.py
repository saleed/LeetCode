class MyCalendar(object):

    def __init__(self):
        self.calendar=[]

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if len(self.calendar)==0:
            self.calendar.append([start,end])
            return True

        for v in self.calendar:
            if start>=v[1] or end<=v[0]:
                continue
            else:
                return False
        self.calendar.append([start,end])
        return True


    def book2(self,start,end):


    def binarySearch(self,start,end):


















# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
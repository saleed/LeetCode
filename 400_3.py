#超出时间限制
class Solution:
    def findNthDigit1(self, n: int) -> int:

        count=0
        cur= 1

        while True:
            l=self.digitNumOf(cur)
            if count+l<n:
                count+=l
                cur+=1
            else:
                break
        left=l+count-n+1
        k=0
        while left>0:
            k=cur%10
            cur=int(cur/10)
            left-=1
        return k


    def digitNumOf(self,n):
        count=0
        while n:
            count+=1
            n=int(n/10)
        return count




    def findNthDigit2(self,n):




a=Solution()

print(a.digitNumOf(100))
print(a.findNthDigit(3))
print(a.findNthDigit(11))
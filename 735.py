class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        if len(asteroids)==0:
            return []
        i=0
        while i<len(asteroids):
            print(i)
            if i==0 or (asteroids[i]>0 and asteroids[i-1]<0 ) or asteroids[i]* asteroids[i-1]>0:
                i+=1
            else:
                if abs(asteroids[i]) == abs(asteroids[i-1]):
                    asteroids=asteroids[:i-1]+asteroids[i+1:]
                    i=max(0,i-2)
                elif abs(asteroids[i])>abs(asteroids[i-1]):
                    asteroids=asteroids[:i-1]+asteroids[i:]
                    i=i-1
                else:
                    asteroids = asteroids[:i] + asteroids[i+1:]
        return asteroids

asteroids =[8,-8]

a=Solution()
print(a.asteroidCollision(asteroids))

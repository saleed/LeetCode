class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.height = height
        self.width = width
        self.food = []
        for i in range(len(food))[::-1]:
            self.food.append(food[i])

        self.pos = [0, 0]
        self.length=0
        self.body=[0]

    def move(self, direction):
        """
        :type direction: str
        :rtype: int
        """
        if direction == "D":
            if self.pos[0] +1 >=self.height:
                return -1
            else:
                self.pos[0] += 1
        elif direction == "U" :
            if self.pos[0] - 1 <0:
                return -1
            else:
                self.pos[0] -= 1

        elif direction == "L" :
            if self.pos[1] - 1 < 0:
                return -1
            else:
                self.pos[1] -= 1

        elif direction == "R":
            if self.pos[1] + 1 >= self.width:
                return -1
            else:
                self.pos[1] += 1


        if len(self.food)>0 and self.pos[0]==self.food[-1][0] and self.pos[1]==self.food[-1][1]:
            self.length+=1
            self.food.pop()
        else:
            self.body=self.body[1:]

        if self.hitbody(self.pos[0], self.pos[1]): ####
            return False

        self.body.append(self.pos[0] * self.width + self.pos[1])

        return self.length


    def hitbody(self,i,j):
        if i*self.width+j in self.body:
            return True
        return False





# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

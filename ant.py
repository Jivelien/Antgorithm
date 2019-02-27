import random

class ant():
    def __init__(self,x = 50, y=50):
        self.y = y
        self.x = x
        self.food = False
            
    def move(self,size : tuple):
        self.y = min(max(self.y + random.randrange(-1,2,1), 0), size[0] - 1)
        self.x = min(max(self.x + random.randrange(-1,2,1), 0), size[1] - 1)
        
        
    def getParam(self):
        return {'y':self.y , 'x':self.x, 'food':self.food}

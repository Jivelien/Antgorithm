import random

class ant():
    def __init__(self,x = 50, y=50):
        self.y = y
        self.x = x
        self.food = False
            
    def move(self):
        self.y = min(max(self.y + random.randrange(-1,2,1), 0), 98)
        self.x = min(max(self.x + random.randrange(-1,2,1), 0), 98)
        
        
    def getParam(self):
        return {'x':self.x, 'y':self.y, 'food':self.food}

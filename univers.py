import numpy as np
from ant import ant

class poi(object): # point of interest
    def __init__(self, y : int, x : int):
        self.y = y
        self.x = x
    
    def pos(self):
        return {'y' : self.y, 'x' : self.x}
    
class univers(object):
    def __init__(self,uniY : int, uniX : int, population : int = 100):
        self.world = np.array(np.zeros((uniY,uniX)))
        self.food = poi(100, 100)
        self.home = poi(int(uniY/2), int(uniY/2))
        
        self.population = []
        for i in range(population):
            self.population.append(ant(self.home.y, self.home.x))
    
    def timeFly(value : int, speed : int):
        return max(value - speed, 0)
    timeFly_v=np.vectorize(timeFly)

    def moveAll(self):
        for a in self.population:
            a.move(self.world.shape)
    
    def showAll(self):
        for a in self.population:
            self.world[a.y,a.x]=255
    
    def applyTime(self, time : int = 10):
        self.world = self.timeFly_v(self.world, time)
        self.moveAll()
        self.showAll()

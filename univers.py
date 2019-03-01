import numpy as np
from ant import ant
from random import randrange

class poi(object): # point of interest
    def __init__(self, y : int, x : int):
        self.y = y
        self.x = x
    
    def pos(self):
        return {'y' : self.y, 'x' : self.x}
    
class univers(object):
    def __init__(self,uniY : int, uniX : int, population : int = 100):
        self.world = np.array(np.zeros((uniY,uniX)))
        
        self.ant_position = np.array(np.zeros((uniY,uniX)))
        self.path_from_home = np.array(np.zeros((uniY,uniX)))
        self.path_from_food = np.array(np.zeros((uniY,uniX)))
        
        self.food = poi(randrange(0,uniY), randrange(0,uniX))
        self.home = poi(int(uniY/2), int(uniY/2))
        
        self.population = []
        self.maxPop = population 
    
    def antBirth(self):
        if self.maxPop > len(self.population):
            self.population.append(ant(self.home.y, self.home.x))
    
    
    def timeFly(value : int, speed : int, frame : int, power : int):
        return max(value - int(frame%speed == 0) * power, 0)
    timeFly_v=np.vectorize(timeFly)

    def moveAll(self):
        for a in self.population:
            a.move(self)
    
    def showAll(self):
        self.ant_position[:, :] = 0
        for a in self.population:
            if not a.food:
                self.path_from_home[a.y, a.x] = min(self.path_from_home[a.y, a.x] + max(min(255,  255 - (a.step // 4)),0),255)  
            else:
                self.path_from_food[a.y, a.x] = min(self.path_from_food[a.y, a.x] + max(min(255,  255 - (a.step // 4)),0),255)  
            self.ant_position[a.y, a.x] = 255
        #self.population=[a for a in self.population if a.step < 100]
    
    def applyTime(self, speed : int, frame : int, power : int):
        self.antBirth()
        self.path_from_home = self.timeFly_v(self.path_from_home, speed, frame, power)
        self.path_from_food = self.timeFly_v(self.path_from_food, speed, frame, power)
        self.moveAll()
        self.showAll()


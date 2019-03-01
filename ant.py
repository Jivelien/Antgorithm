import random
import numpy as np

global BLANK_WEIGHT
BLANK_WEIGHT = 50

class ant(object):
    def __init__(self,x = 50, y=50):
        self.y = y
        self.x = x
        self.food = False
        self.step = 0
    
    def nextPosition(self, path_map, blank_weight = BLANK_WEIGHT):
        size= path_map.shape
        neighbour = path_map[
                    max(self.y-1, 0):min(self.y +2,size[0]),
                    max(self.x-1, 0):min(self.x +2,size[1])
                    ]
        weightNeighbour = (neighbour + blank_weight )
        weightNeighbour = weightNeighbour / weightNeighbour.sum()
        neighbourRow = neighbour.reshape(neighbour.size)     
        weightNeighbourRow = weightNeighbour.reshape(neighbour.size)
        
        peakValue = np.random.choice(neighbourRow, p = weightNeighbourRow)
        locate = np.where(neighbour==peakValue)
        
        random_in_select = random.randint(1, locate[0].size)
        
        self.y += locate[0][random_in_select - 1] - int(max(self.y-1, 0) == self.y-1)
        self.x += locate[1][random_in_select - 1] - int(max(self.x-1, 0) == self.x-1)

    
    def move(self, univers):
        if not self.food:
            self.nextPosition(univers.path_from_food, 50)
        else:
            self.nextPosition(univers.path_from_home, 50)
            
        #self.y = min(max(self.y + random.randrange(-1,2,1), 0), size[0] - 1)
        #self.x = min(max(self.x + random.randrange(-1,2,1), 0), size[1] - 1)
                
        if not self.food and univers.food.x == self.x and univers.food.y == self.y:  
            print('I find the food ! x: {}, y:{} in {} steps'.format(self.x,self.y, self.step))
            self.step = 0
            self.food = True
        elif self.food and univers.home.x == self.x and univers.home.y == self.y:
            print('I find home ! x: {}, y:{} in {} steps'.format(self.x,self.y, self.step))
            self.step = 0
            self.food = False          
        else:
                self.step += 1
        
    def getParam(self):
        return {'y':self.y, 
                'x':self.x, 
                'food':self.food, 
                'step':self.step}

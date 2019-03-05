import random
import numpy as np

def weightedSelection(neighbour : np.array):
        return neighbour * neighbour*0.5
    
class ant(object):
    def __init__(self,y = 50, x=50, weightSelect = weightedSelection):
        self.y = y
        self.x = x
        self.food = False
        self.step = 0
        self.weightSelect = weightSelect
    
    def nextPosition(self, path_map, blank_weight = 5):
        size= path_map.shape
        neighbour = path_map[
                    max(self.y-1, 0):min(self.y +2,size[0]),
                    max(self.x-1, 0):min(self.x +2,size[1])
                    ].astype('int')
        
        wNeighbour = self.weightSelect(neighbour) + blank_weight
        wNeighbour = wNeighbour / wNeighbour.sum()
        
        neighbourRow = neighbour.reshape(neighbour.size)     
        wNeighbourRow = wNeighbour.reshape(neighbour.size)
        
        peakValue = np.random.choice(neighbourRow, p = wNeighbourRow)
        locate = np.where(neighbour==peakValue)
        
        random_in_select = random.randint(1, locate[0].size)
        
        self.y += locate[0][random_in_select - 1] - int(max(self.y-1, 0) == self.y-1)
        self.x += locate[1][random_in_select - 1] - int(max(self.x-1, 0) == self.x-1)

    
    def move(self, univers):
        if not self.food:
            self.nextPosition(univers.path_from_food)
        else:
            self.nextPosition(univers.path_from_home)
            
        #self.y = min(max(self.y + random.randrange(-1,2,1), 0), size[0] - 1)
        #self.x = min(max(self.x + random.randrange(-1,2,1), 0), size[1] - 1)
                
        if univers.food.x == self.x and univers.food.y == self.y:  
                self.step = 0
                self.food = True
        elif univers.home.x == self.x and univers.home.y == self.y:
                if self.food:
                    univers.score +=1
                self.step = 0
                self.food = False          
        else:
                self.step += 1
        
    def getParam(self):
        return {'y':self.y, 
                'x':self.x, 
                'food':self.food, 
                'step':self.step}

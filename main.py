import cv2
from univers import univers
from matplotlib import pyplot as plt
import random as ran 

def main():
    cv2.startWindowThread()
    
    universY=100
    universX=int(universY*16/9)
       
    univParam = {'uniY' : universY, 
                 'uniX' : universX, 
                 'population' : 500, #ran.randrange(100,5000), 
                 'exhaust' : ran.randrange(1000,10000), 
                 'stepWeight' : ran.randrange(10,255), 
                 'weightLostByStep' : ran.randrange(1,10),
                 'lostEachEpoch' : ran.randrange(1,10),
                 'lostPower' : ran.randrange(1,10)}

    u = univers(**univParam)
   # u.food.y = 15
   # u.food.x = 15
    
    cBLUE=0
    cGREEN=1
    cRED=2

    cv2.namedWindow("Anthology", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Anthology",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)


    while True:
        u.applyTime()
        
        posAnt = u.ant_position.astype('uint8')
        pathHome = u.path_from_home.astype('uint8')
        pathFood = u.path_from_food.astype('uint8')
        
        canva = cv2.cvtColor(u.world.astype('uint8'), cv2.COLOR_GRAY2RGB)
        #canva[:,:,cRED]     = posAnt
        canva[:,:,cBLUE]    = pathHome
        canva[:,:,cGREEN]   = pathFood
        canva[u.food.y, u.food.x, cRED] = 255
        
        cv2.putText(canva, str(u.score), (10,10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255,255,255), 1)
        
        cv2.imshow('Anthology', canva) 
        #cv2.imshow('Anthology', cv2.resize(canva,(900,900),interpolation = 0)) 
        
        k = cv2.waitKey(1) & 0xFF
        if k == ord('q'):
            cv2.destroyAllWindows()
            break
    #sleep(1/1000)
    return u

u = main()

def nothing(): 
    universY=100
    universX=int(universY*16/9)
    
    u = univers(universY,universX,
                population = 1000,
                exhaust = 2000)
    u.food.y = 25
    u.food.x = 45
    try:
        while True:
            u.applyTime(1, 1)
    except:
        plt.subplot(2,1,1)
        plt.plot(u.scoreList)
        
        plt.subplot(2,1,2)
        cBLUE=0
        cGREEN=1
        cRED=2
        posAnt = u.ant_position.astype('uint8')
        pathHome = u.path_from_home.astype('uint8')
        pathFood = u.path_from_food.astype('uint8')
        
        canva = cv2.cvtColor(u.world.astype('uint8'), cv2.COLOR_GRAY2RGB)
        canva[:,:,cRED]     = posAnt
        canva[:,:,cBLUE]    = pathHome
        canva[:,:,cGREEN]   = pathFood
        canva[u.food.y, u.food.x, cRED] = 255
        plt.imshow(canva)
# 0: blue
# 1: vertq
# 2: rouge

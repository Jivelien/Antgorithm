import cv2
import numpy as np
from time import sleep
from univers import univers

def main():
    cv2.startWindowThread()
    
    u = univers(200,200,1000)
    
    cBLUE=0
    cGREEN=1
    cRED=2
    
    i=0
    while True:
        u.applyTime(5, i, 1)
        
        posAnt = u.ant_position.astype('uint8')
        posAnt = cv2.cvtColor(posAnt, cv2.COLOR_GRAY2RGB)
        posAnt[:,:,cBLUE]=0
        posAnt[:,:,cGREEN]=0
        
        pathHome = u.path_from_home.astype('uint8')
        pathHome = cv2.cvtColor(pathHome,cv2.COLOR_GRAY2RGB)
        pathHome[:,:,cRED]=0
        pathHome[:,:,cGREEN]=0
        
        pathFood = u.path_from_food.astype('uint8')
        pathFood = cv2.cvtColor(pathFood,cv2.COLOR_GRAY2RGB)
        pathFood[:,:,cRED]=0
        pathFood[:,:,cBLUE]=0
        
        canva = cv2.add(pathFood,pathHome)
        canva = cv2.add(canva, posAnt)
        
        cv2.imshow('Anthology', cv2.resize(canva,(900,900),interpolation = 0)) #canvaPic)
        #cv2.imshow('Anthology', cv2.resize(path,(900,900),interpolation = 0)) #canvaPic)
        
        k = cv2.waitKey(1) & 0xFF
        if k == ord('q'):
            cv2.destroyAllWindows()
            break
        i += 1
    #sleep(1/1000)

main()

# 0: blue
# 1: vertq
# 2: rouge

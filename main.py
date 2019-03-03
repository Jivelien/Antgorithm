import cv2
from univers import univers
from matplotlib import pyplot as plt

def main():
    cv2.startWindowThread()
    
    u = univers(100,100,
                population = 1000,
                exhaust = 3000)
    
    cBLUE=0
    cGREEN=1
    cRED=2
    
    i=0
    while True:
        u.applyTime(3, i, 1)
        
        posAnt = u.ant_position.astype('uint8')
        pathHome = u.path_from_home.astype('uint8')
        pathFood = u.path_from_food.astype('uint8')
        
        canva = cv2.cvtColor(u.world.astype('uint8'), cv2.COLOR_GRAY2RGB)
        #canva[:,:,cRED]     = posAnt
        canva[:,:,cBLUE]    = pathHome
        canva[:,:,cGREEN]   = pathFood
        
        cv2.putText(canva, str(u.score), (10,10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255,255,255), 1)
        
        cv2.imshow('Anthology', cv2.resize(canva,(900,900),interpolation = 0)) #canvaPic)
        #cv2.imshow('Anthology', cv2.resize(path,(900,900),interpolation = 0)) #canvaPic)
        
        k = cv2.waitKey(1) & 0xFF
        if k == ord('q'):
            cv2.destroyAllWindows()
            break
        i += 1
    #sleep(1/1000)
    return u

u = main()
plt.plot(u.scoreList)

# 0: blue
# 1: vertq
# 2: rouge

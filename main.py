import numpy as np
import cv2
from scipy import ndimage
from time import sleep
from ant import ant

canvaY = 99
canvaX = 99

def createCanva():
    return np.zeros((canvaY,canvaX), dtype='uint8')

def timeFly(value : int, speed : int):
    return max(value - speed, 0)
timeFly_v=np.vectorize(timeFly)


def moveAll(ants):
    for a in ants:
        a.move()

def showAll(canva, ants):
    for a in ants:
        canva[a.y,a.x]=255
    return canva


cv2.startWindowThread()

ants = []
for i in range(1000):
    ants.append(ant())
canva = createCanva()

while True:
    moveAll(ants)
    canva = showAll(canva,ants)
    
    
    canvaPic=ndimage.zoom(canva.astype('uint8'), zoom=5, order = 0)
    cv2.imshow('life', canvaPic)
    
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        cv2.destroyAllWindows()
        break
    
    sleep(1/1000)
    canva=timeFly_v(canva,25)
    

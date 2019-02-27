import cv2
from scipy import ndimage
from time import sleep
from univers import univers


cv2.startWindowThread()

u = univers(200,200,500)

while True:
    u.applyTime(5)
    
    canvaPic=ndimage.zoom(u.world.astype('uint8'), zoom=3, order = 0)
    cv2.imshow('life', canvaPic)
    
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        cv2.destroyAllWindows()
        break
    
    #sleep(1/1000)
    
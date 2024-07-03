from random import randint

import cv2
import numpy as np

from anthgorithm.ant import Ant
from anthgorithm.position import Position


def visualisation_biscuit():
    cv2.startWindowThread()

    cv2.namedWindow("Anthology", cv2.WND_PROP_ASPECT_RATIO)
    cv2.setWindowProperty("Anthology", cv2.WND_PROP_AUTOSIZE, cv2.WINDOW_GUI_EXPANDED)

    ant = Ant(position=Position(x=0, y=0))

    canva_x = 1000
    canva_y = 1000
    while True:
        world = np.array(np.zeros((canva_x, canva_y)))
        canva = cv2.cvtColor(world.astype('uint8'), cv2.COLOR_GRAY2RGB)

        x = int(ant.position.x + canva_x/2)%canva_x
        y = int(ant.position.y + canva_y/2)%canva_y

        cv2.circle(canva, center=(x,y), radius=10, color=(0,0,255), thickness=5)
        cv2.imshow('Anthology', canva)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('q'):
            cv2.destroyAllWindows()
            break

        ant.rotate(angle=randint(-30, 30))
        ant.move()


if __name__ == '__main__':
    visualisation_biscuit()

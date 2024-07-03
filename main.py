from random import randint

import cv2
import numpy as np

from anthgorithm.ant import Ant
from anthgorithm.ant_brain.ant_brain import RandomAntBrain
from anthgorithm.position import Position


def visualisation_biscuit():
    cv2.startWindowThread()

    cv2.namedWindow("Anthology", cv2.WND_PROP_ASPECT_RATIO)
    cv2.setWindowProperty("Anthology", cv2.WND_PROP_ASPECT_RATIO, cv2.WINDOW_GUI_EXPANDED)

    nb_ant=50

    ants = [Ant(ant_brain=RandomAntBrain(angle=15)) for _ in range(nb_ant)]
    for i, ant in enumerate(ants):
        ant.rotate(randint(0,360))

    max_rotation=5
    colors = [(randint(0,255),randint(0,255),randint(0,255)) for _ in range(nb_ant)]

    canva_x = 2000
    canva_y = int(2000*16/9)
    while True:
        world = np.array(np.zeros((canva_x, canva_y)))
        canva = cv2.cvtColor(world.astype('uint8'), cv2.COLOR_GRAY2RGB)

        for i, ant in enumerate(ants):
            ant.move()
            x = int(ant.current_position.x + canva_x / 2) % canva_x
            y = int(ant.current_position.y + canva_y / 2) % canva_y

            cv2.circle(canva, center=(y,x), radius=10, color=colors[i], thickness=5)
        cv2.imshow('Anthology', canva)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('q'):
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    visualisation_biscuit()

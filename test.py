import numpy as np
import cv2
from mss import mss
import time

mon = {'top': 22, 'left': 28, 'width': 800, 'height': 640}
sct = mss()
last_time = time.time()
while 1:
    img = np.array(sct.grab(mon))
    print('loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()
    cv2.imshow('test', cv2.resize(np.array(img),(800,640)))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
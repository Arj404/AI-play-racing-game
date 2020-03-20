import numpy as np
import cv2
from mss import mss
import time

def screen_record(): 
    mon = {'top': 22, 'left': 28, 'width': 400, 'height': 320}
    sct = mss()
    last_time = time.time()
    while (True):
        img = np.array(sct.grab(mon))
        p_img = process_img(img)
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('test', cv2.resize(np.array(p_img),(800,640)))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
def process_img(image):
    original_image = image
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    processed_img =  cv2.Canny(processed_img, threshold1 = 200, threshold2=300)
    return processed_img

# screen_record()
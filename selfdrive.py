import numpy as np
from PIL import ImageGrab
import cv2
import time
#import pyautogui

#for i in list(range(4))[::-1]:
 #   print(i+1)
  #  time.sleep(1)

#print('down')
#pyautogui.keyDown('w') 
#time.sleep(3)
#print('up')
#pyautogui.keyUp('w') 

def process_img(image):
    original_image = image
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    processed_img =  cv2.Canny(processed_img, threshold1 = 200, threshold2=300)
    return processed_img



last_time = time.time()
while True:
    screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
    last_time = time.time()
    new_screen = process_img(screen)
    cv2.imshow('window', new_screen)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
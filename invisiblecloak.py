import cv2
import numpy as np
import time

print(cv2.__version__)

raw_video = cv2.VideoCapture("video.mp4")

time.sleep(1)
count=0
background = 0

# the video has some seconds in the start where the background is completely visible, capturing that background which would be used for masking later
for i in range(60):
    return_val, background = raw_video.read()
    if return_val == False:
        continue
    elif not return_val or background is None: 
        print("Error: Could not read frame from camera.")
        continue
# to join hands one hand has to be the mirror image of the other 

background = np.flip(background, axis=1)

while(raw_video.isOpened()):
    return_val, img = raw_video.read()
    if not return_val:
        break
    count +=1
    # flipping the image for consistency
    img = np.flip(img, axis=1)
    
    # converting the color from BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # generating mask to detect red color
    lower_red = np.array([100, 40, 40])
    upper_red = np.array([100, 255, 255])
   
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([155, 40, 40])
    upper_red = np.array([180, 255, 255])
   
    mask2 = cv2.inRange(hsv, lower_red, upper_red)
    mask1 = mask1 + mask2          

   # for refining the image asimage is raw and blurry after processing into hsv
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    mask1 = cv2.dilate(mask1, np.ones((3, 3), np.uint8), iterations=1)

    mask2 = cv2.bitwise_not(mask1)

    #The masking happens here. You are adding two images together
    res1 = cv2.bitwise_and(background, background, mask=mask1)
    res2 = cv2.bitwise_and(img, img, mask=mask2)
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    cv2.imshow("INVISIBLE MAN", final_output)
    k = cv2.waitKey(10)
    if k == 27:
        break
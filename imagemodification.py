# save an image using opencv after doing some changes
import cv2
import os

# change the path to where you wish to save the image
saved_directory = "C:/Users/yosin/Pictures"


img = cv2.imread("pika.png", 0)
cv2.imshow("Pikachu in BLACK AND WHITE", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# change the current execution directory
os.chdir(saved_directory)

# write image to this directory
cv2.imwrite("pikablackandwhite.png",img)
print ("Successfully saved")
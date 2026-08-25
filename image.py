import cv2

# imread is used to an image by passing the path of the image as an input
img = cv2.imread("pika.png", cv2.IMREAD_COLOR)

# there are three parameters to write an image
# cv2.IMREAD_COLOR(1) => specify to load the image in color
# cv2.IMREAD_GRAYSCALE(0) => specify to load the image in grayscale/ black & white
# cv2.IMREAD_UNCHANGED(-1) => specify to load the image unchanged

# imshow is used to show the loaded image in a new  window with a title
cv2.imshow(" Pikachu image", img)

# to hold the window until the user presses any key
cv2.waitKey(0)

# delete / close the image window after the key is pressed
cv2.destroyAllWindows(0)


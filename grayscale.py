import cv2

img = cv2.imread("pika.png", 0)
cv2.imshow("Pikachu in grayscale", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
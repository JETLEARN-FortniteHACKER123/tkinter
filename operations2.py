import cv2
img = cv2.imread("pika.png")
cv2.imshow("Original Image", img)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

image = cv2.imread("pika.png")
(row, col) = image.shape[0:2]

for i in range(row):
    for j in range(col):
        image[i,j] = sum(image[i,j])*0.33
cv2.imshow("Grayscale Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread("pika.png")
M = cv2.getRotationMatrix2D((col/2, row/2), 45, 1)
res = cv2.warpAffine(img, M, (col, row))
cv2.imwrite("result.jpg", res)

image = cv2.imread("pika.png")
edges = cv2.Canny(image, 100, 200)
cv2.imwrite("edges.jpg", edges)


image = cv2.imread("pika.png")
hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV Image", hsvImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
image = cv2.imread("pika.png")

# start coordinates here(0,0)represents the top left corner of the image)
start_point = (0, 0)
# end coordinates here(900, 900)represents the bottom right corner of the image)
end_point = (900, 900)
# Green color in bgr
color = (0, 255, 0)
# Line thickness of 9 px
thickness = 9
# Using cv2.line() method
# draw a diagonal green line with thickness of 9 px
image = cv2.line(image, start_point, end_point, color, thickness)
cv2.imshow("Line", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

image = cv2.imread("pika.png")
start_point = (0, 0)
end_point = (850, 850)
color = (255,0,0)
thickness = 2
color2 = (0, 0, 0)
thickness2 = -1
image = cv2.rectangle(image, start_point, end_point, color, thickness)
image = cv2.rectangle(image, start_point, end_point, color2, thickness2)
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
image = cv2.imread("pika.png")
# centre coordinates of the circle
center_coordinates = (450, 450)
# radius of the circle
radius = 150
color = (0, 0, 255)
color2 = (0, 255, 0)
# Line thickness of 2 px
thickness = 2
thickness2 = -1
# Using cv2.circle() method
image = cv2.circle(image, center_coordinates, radius, color, thickness)
image = cv2.circle(image, center_coordinates, radius, color2, thickness2)
#displaying the image
cv2.imshow("Circle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

image= cv2.imread("pika.png")
# font
font = cv2.FONT_HERSHEY_SIMPLEX
# org
org = (50, 50)
#fontscale
fontScale = 1
# Blue color in BGR
color = (0, 0, 255)
# Line thickness of 2 px
thickness = 2
# Using cv2.putText() method
image = cv2.putText(image, 'Pikachu', org, font, fontScale, color, thickness, cv2.LINE_AA)
cv2.imshow("Text", image)
cv2.waitKey(0)
cv2.destroyAllWindows()



image = cv2.imread("pika.png")
start_point1 = (200, 0)
start_point2 = (0, 200)
end_point1 = (200,800)
end_point2 = (200, 400)

color1 = (0,0,255)
color2 = (0,255,0)
thickness1 = 9
thickness2 = 9
image = cv2.line(image, start_point1, end_point1, color1, thickness1)
image = cv2.line(image, start_point2, end_point2, color2, thickness2)
cv2.imshow("Lines", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

image = cv2.imread("pika.png")
start_point = (0, 0)
end_point = (900, 900)
color = (0, 255, 0)
thickness = 5
image = cv2.rectangle(image, start_point, end_point, color, thickness)
font = cv2.FONT_HERSHEY_SIMPLEX
org = (50, 50)
fontScale = 1
color = (255, 0, 0)
thickness = 2
image = cv2.putText(image, 'Hello, Pikachu!', org, font, fontScale, color, thickness, cv2.LINE_AA)
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
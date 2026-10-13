import cv2
import os
from PIL import Image  # pillow - image processing library python imaging system

# change directory to where the images are stored
os.chdir("C:\\photos")
path = "C:\\photos"

mean_height = 0
mean_width = 0

num_of_images = len(os.listdir('.'))
for file in os.listdir('.'):
    im = Image.open(os.path.join(path, file))
    width, height = im.size
    mean_width = mean_width + width
    mean_height =mean_height + height

mean_width = mean_width // num_of_images
mean_height = mean_height // num_of_images

print('Mean Width:', mean_width)
print('Mean Height:', mean_height)

for file in os.listdir('.'):
    if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg'):
        im = Image.open(os.path.join(path, file))
        width, height = im.size
        print(width, height)

        imresized = im.resize((mean_width, mean_height), Image.LANCZOS)
        imresized.save(file, 'JPEG', quality=95)
        print(im.filename.split('\\')[-1], " is resized  ")

def videoGenerator():
    video_name = "Myfirstvideo.avi"

    os.chdir("C:\\photos")

    images = []
    for im in os.listdir('.'):
        if im.endswith('.jpg') or im.endswith('.png') or im.endswith('.jpeg'):
            images.append(im)
    print(images)

    frame = cv2.imread(os.path.join(path, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 1, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(".", image)))       

    cv2.destroyAllWindows()
    video.release()

videoGenerator()    
import cv2 as cv2
from skimage.color import rgb2gray

filename = 'Test2.mp4'

video = cv2.VideoCapture(filename)
framesNo = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

cnt = 0
for i in range(0,1):
    print(video.read()[1])
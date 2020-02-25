import zmq
import sys
import numpy as np
from skimage.color import rgb2gray
import cv2 as cv

#processing_function:
def process(img,frameNo):
    grayImage= rgb2gray(img)
    data = {
        'frameNo' : frameNo,
        'frame' : grayImage
    }
    return data

#ports:
N = int(sys.argv[1])
binPort = int(sys.argv[2])
print("Producer")
print(str(binPort))

#reading video:
vidPath= sys.argv[3]
videoData = cv.VideoCapture(vidPath)
framesCount = int(videoData.get(cv.CAP_PROP_FRAME_COUNT))
framesCount= min(501,framesCount+1)


#connection:
context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind("tcp://25.74.93.108:%s" % binPort)

#processing:
frameNo = 1
for frameNo in range (1,framesCount):
    frame = videoData.read()[1]
    #send one frame every 30 frame
    data = process(frame,frameNo)
    #sending
    socket.send_pyobj(data)
    # print(frameNo)

#finish:
data = { 'frame' : None}
for i in range (0,N):
    socket.send_pyobj(data)
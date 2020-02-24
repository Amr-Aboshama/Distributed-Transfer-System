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
binPort = int(sys.argv[1])

#reading video:
vidPath= sys.argv[2]
videoData = cv.VideoCapture(vidPath)
framesCount = int(videoData.get(cv.CAP_PROP_FRAME_COUNT))
framesCount= min(500,framesCount+1)

#connection:
context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind("tcp://127.0.0.1:%s" % binPort)

#processing:
frameNo = 1
for frameNo in range (1,framesCount):
    frame = videoData.read()[1]
    #send one frame every 30 frame
    data = process(frame,frameNo)
    #sending
    socket.send_pyobj(data)

#finish:
data = { 'frame' : None}
socket.send_pyobj(data)
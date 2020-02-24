import zmq
import sys
import numpy as np
from skimage.filters import threshold_otsu

#otsu:
def otsu_th(img):
    threshould= threshold_otsu(img)
    binaryImage=np.zeros((img.shape))
    binaryImage= img > threshould
    return binaryImage

#ports:
producerPort = int(sys.argv[1])
collectorPort = int(sys.argv[2])

#connection:
context = zmq.Context()
#pulling connection:
socketPull = context.socket(zmq.PULL)
socketPull.connect("tcp://127.0.0.1:%s" % producerPort)
#Pushing connection:
socketPush = context.socket(zmq.PUSH)
socketPush.connect("tcp://127.0.0.1:%s" % collectorPort)

#processing:
while True:
    #recieve:
    recData = socketPull.recv_pyobj()
    if recData['frame'] is None:
        break
    #process:
    processedFrame = otsu_th (recData['frame'])
    sentData = {
        'frameNo' : recData['frameNo'],
        'otsu' : processedFrame
    }
    #send:
    socketPush.send_pyobj(sentData)

#finish:
endPoint = {'otsu' : None}
socketPush.send_pyobj(endPoint)
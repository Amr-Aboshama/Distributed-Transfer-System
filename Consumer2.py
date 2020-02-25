import zmq
import sys
import numpy as np
from skimage.measure import find_contours

def getContours(mat):
    cont = find_contours(mat,0.8)
    ret = []
    for c in cont:
        Xmax,Xmin,Ymax,Ymin = max(c[:,1]), min(c[:,1]), max(c[:,0]), min(c[:,0])
        ret.append([Xmin,Ymin,Xmax,Ymax])
    return ret

# PullPort PushPort
pullPort = int(sys.argv[1]) #5557
pushPort = int(sys.argv[2]) #5556

print("Consumer2")
print("Pull: " + str(pullPort) + " Push: " + str(pushPort))

context = zmq.Context()

otherMachineIP = "25.74.93.108"


#Pulling
socketPull = context.socket(zmq.PULL)
#
socketPull.connect("tcp://" + otherMachineIP + ":%s" % pullPort)

#Pushing
socketPush = context.socket(zmq.PUSH)
socketPush.connect("tcp://25.1.34.71:%s" % pushPort)


while True:
    data = socketPull.recv_pyobj()
    if data['otsu'] is None:
        break

    obj = { 'frameNo' : data['frameNo'],
            'contours' : getContours(data['otsu'])
            }
    # print(data['frameNo'])
    socketPush.send_pyobj(obj)

obj = {'contours' : None}
socketPush.send_pyobj(obj)
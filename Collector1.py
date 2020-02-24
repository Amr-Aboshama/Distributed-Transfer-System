import zmq
import sys
import numpy as np

#ports:
N = int(sys.argv[1])
pullPort = int(sys.argv[2])
pushPort = int(sys.argv[3])

otherMachineIP = "127.0.0.1"

#connection:
context = zmq.Context()
#pulling connection:
socketPull = context.socket(zmq.PULL)
socketPull.bind("tcp://127.0.0.1:%s" % pullPort)
#Pushing connection:
socketPush = context.socket(zmq.PUSH)
socketPush.bind("tcp://" + otherMachineIP + ":%s" % pushPort)


finished = 0
while True:
    #recieve:
    recData = socketPull.recv_pyobj()
    if recData['otsu'] is None:
        finished = finished + 1
        if finished == N :
            break
    #send:
    socketPush.send_pyobj(recData)

#finish:
endPoint = {'otsu' : None}
socketPush.send_pyobj(endPoint)
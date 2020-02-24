import zmq
import numpy as np

port = 5556
context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.bind("tcp://127.0.0.1:%s" % port)

print("Waiting!")
data=socket.recv_pyobj()
print("DATA RECEIVED!")
print(data)
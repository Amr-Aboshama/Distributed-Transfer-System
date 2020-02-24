import zmq
import numpy as np

port = 5556
context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.connect("tcp://127.0.0.1:%s" % port)


A = np.ones((3,3))
socket.send_pyobj(A)
print("DATA SENT!")
print(A)
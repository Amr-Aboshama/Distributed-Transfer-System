import zmq
import sys
import numpy as np

def writeFile(lst,f,OF):
    OF.write('Frame #' + str(f) + ':\n' + 'No. Contours: ' + str(len(lst)) + '\n')
    for c in lst:
        OF.write('\t* Xmin: ' + str(c[0]))
        OF.write('\tYmin: ' + str(c[1]))
        OF.write('\tXmax: ' + str(c[2]))
        OF.write('\tYmax: ' + str(c[3]) + '\n')

# Conusmers# Port
N = int(sys.argv[1]) #1
port = int(sys.argv[2]) #5556
context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.bind("tcp://127.0.0.1:%s" % port)

finished = 0
frame = 0
outFile = open('Output.txt','w')

while finished < N:
    data = socket.recv_pyobj()
    if data['contours'] is None:
        finished += 1
    else:
        frame += 1
        writeFile(data['contours'],data['frameNo'],outFile)

outFile.close()
import zmq
import numpy as np
import skimage.io as io
from skimage.color import rgb2gray
from skimage.filters import threshold_otsu

port = 6666
context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind("tcp://127.0.0.1:%s" % port)

img = io.imread('golf.jpeg')
img = rgb2gray(img)
binary = np.zeros((img.shape))
binary[img>=threshold_otsu(img)] = 1

obj = {
    'frameNo'   : 1,
    'otsu'      : binary
}

socket.send_pyobj(obj)


obj['otsu'] = None
socket.send_pyobj(obj)


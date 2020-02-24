import sys
import os
from math import ceil

N = int(sys.argv[1])
startPort = int(sys.argv[2])

consumerPort = startPort+ceil(N/2)+1
collectorPort = startPort + 2*ceil(N/2) + 1

for i in range(0,N):
    os.system('start cmd /k py Consumer2.py ' + str(consumerPort) + ' ' + str(collectorPort))
    if i%2!=0:
        consumerPort += 1

os.system('start cmd /k py Collector2.py ' + str(N) + ' ' + str(collectorPort))
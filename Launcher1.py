import sys
import os
from math import ceil

N = int(sys.argv[1])
startPort = int(sys.argv[2])
videoPath = sys.argv[3]

producerPort = startPort
collectorPullPort = startPort+1
collectorPushPort = collectorPullPort + ceil(N/2)

for i in range(0,N):
    #Run Consumer1
    os.system('start cmd /k py Consumer1.py ' + str(producerPort) + ' ' + str(collectorPullPort))
    
    if i%2!=0:
        #Run Collectors1
        os.system('start cmd /k py Collector1.py 2' + str(collectorPullPort) + ' ' + str(collectorPushPort))
        collectorPullPort += 1
        collectorPushPort += 1
if N%2!=0:
        os.system('start cmd /k py Collector1.py 1' + str(collectorPullPort) + ' ' + str(collectorPushPort))

#Run Producer
os.system('start cmd /k py Producer.py ' + str(N) + ' ' + str(producerPort) + ' ' + str(videoPath))
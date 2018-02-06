import sys
import threading
from threading import Thread
from connect import sendDataToFire
sys.path.append('../')
from renderQuery import queryG, queryY, web



def prepareTOsend():
    while True:
        sendDataToFire(json.dumps(queryG))
        prepareTOsend()
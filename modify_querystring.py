from mitmproxy import http
import re
import json
import sys
import threading
import time
from threading import Thread
sys.path.append('../')
from connect import sendDataToFire

queryG = []
queryY = []
web = []

def request(flow: http.HTTPFlow) -> None:
    #data['time'] = flow.request.timestamp_start
    ######################################################################
    if flow.request.url[:32] == "https://www.google.co.in/search?" and flow.request.method == 'GET' :
        #data['From'] = "Google search"
        s = flow.request.path
        s = s[s.find('q=')+2:]
        s = s[:s.find('&')]
        queryG.append(s.replace('+', ' '))
        sendDataToFire(json.dumps(queryG))
    ########################################################################
    elif (flow.request.url[:50] == "https://suggestqueries.google.com/complete/search?" and flow.request.method == 'GET'):
        ys = flow.request.path
        ys = ys[ys.find('q=')+2:]
        ys = ys[:ys.find('&')]
        queryY.append(ys.replace('+', ' '))
    #####################################################################    else:
        if flow.request.method == 'GET':            
            web.push(str(flow.request.host))
    thread.start_new_thread(prepareTOsend())#thread.start_new_thread(prepareTOsend,('prepareTOsend',1))



def prepareTOsend():
    while True:
        sendDataToFire(json.dumps(queryG))
        prepareTOsend()



# if __name__ == '__main__':
#     Thread(target = request).start()
    
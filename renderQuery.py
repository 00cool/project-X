from mitmproxy import http
import re
import json
import sys
import threading
import time
import signal, os
from threading import Thread
sys.path.append('../')
from connect import sendDataToFire


data = {
    "google" : [],
    "youtube" : [],
    "web" : []
}

def request(flow: http.HTTPFlow) -> None:
    global data
    #print(flow.request.host)
    #print(data["google"])
    if flow.request.host in ["www.google.co.in", "www.google.com", "www.google.co.uk"]:
        #print("pass")
        if flow.request.url[:32] == "https://www.google.co.in/search?" and flow.request.method == 'GET' :
            s = flow.request.path
            s = s[s.find('q=')+2:]
            s = s[:s.find('&')]
            data["google"].append(s.replace('+', ' '))     
        if (flow.request.url[:50] == "https://suggestqueries.google.com/complete/search?" and flow.request.method == 'GET'):
            ys = flow.request.path
            ys = ys[ys.find('q=')+2:]
            ys = ys[:ys.find('&')]
            data["youtube"].append(ys.replace('+', ' '))
    else:           
        data["web"].append(flow.request.host)

def send_to_fire():
    global data
    while True:    
        #print("thread started")
        try:
            jsond = json.dumps(data)
            sendDataToFire(jsond)
            time.sleep(5)
        except:
            raise Exception


Thread(target = send_to_fire).start()

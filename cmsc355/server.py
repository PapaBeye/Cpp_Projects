import socket
import os
import json
import time

HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1243))
s.listen(5)

class Events:
    def __init__(self):
        self.Eventspath = "C:\\Users\\beye1\\Desktop\\Fall_2019_sideproject\\cmsc355\\events\\"
        self.LEventNameF = self.getEventFiles()
        self.Events = {}
        self.EventNames = []
        self.loadJson()
        self.Eiter = iter(self.EventNames)

    def loadJson(self):
        for x in os.listdir(self.Eventspath):
            self.EventNames.append(x.replace(".json",""))
        n = iter(self.EventNames)
        for i in self.LEventNameF:
            with open(i) as f:
                self.Events[next(n)] = json.load(f)
                f.close()

    def getEventMSG(self):
        try:
            return self.Events[next(self.Eiter)]
        except Exception as e:
            pass
        
    def getEventFiles(self):
        return list( self.Eventspath + x for x in (os.listdir(self.Eventspath)))



Eobj = Events()
while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    Req = clientsocket.recv(16)
    for i in Eobj.EventNames:
        msg = Eobj.getEventMSG()
        msg = f"{len(str(msg)):<{HEADERSIZE}}"+str(msg)
        clientsocket.send(bytes(msg,"utf-8"))
        time.sleep(2)
    

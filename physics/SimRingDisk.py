from vpython import *


class simRing:
    def __init__(self):
        self.scene = canvas(width=1200, height=600)
        canvas.selected = self.scene
        self.Q_ring = 0.0
        wtext(pos=self.scene.caption_anchor,text="Enter Charge Q for Ring")
        self.scene.append_to_caption(' ') 
        self.Q_ring_Entry = winput(pos=self.scene.caption_anchor,bind=self.setQring)
        self.scene.append_to_caption(' ') 
        wtext(pos=self.scene.caption_anchor,text="Enter Radius for ring")
        self.scene.append_to_caption(' ') 
        self.Radius_Entry = winput(pos=self.scene.caption_anchor,bind=self.setQring)
        wtext(pos=self.scene.caption_anchor,text="Enter N for Delta Q (Q / N)")
        self.scene.append_to_caption(' ') 
        self.N_Entry = winput(pos=self.scene.caption_anchor,bind=self.setQring)
        self.scene.append_to_caption('\n') 
        wtext(pos=self.scene.caption_anchor,text="Enter Position for Point Charge")
        self.scene.append_to_caption(' ') 
        self.ptChargePOS_Entry = winput(pos=self.scene.caption_anchor,type="string", bind=self.setQring)
        self.scene.append_to_caption(' ') 
        self.Escale_Label = wtext(pos=self.scene.caption_anchor,text="Enter E Scale for Q")
        self.scene.append_to_caption(' ') 
        self.Escale_Entry = winput(pos=self.scene.caption_anchor,bind=self.setQring)
        self.Earrow=arrow(pos=vector(0,0,0),axis=vector(1,0,0),color=color.purple)
        

    def setQring(self, S):
        if S.number:
            self.Q_ring = S.number
            print(self.Q_ring)
    def setPtchar(self, S):
        if str(S.text):
            try:
                ptsQ = S.text
                self.ptChargePOS = vector(float(ptsQ.split(",")[0]), float(ptsQ.split(",")[1]), float(ptsQ.split(",")[2]))
            except Exception as e:
                print(e)
        else:
            self.ptChargePOS = vector(0,0,0)
    def setNchar(self, S):
        if S.number:
            try:
                self.numberOFchargesInRing = int(S.number)
            except Exception as e:
                self.numberOFchargesInRing = 2
                print(e)
        else:
            self.numberOFchargesInRing = 2
    def setEscale(self, S):
        if S.number:
            try:
                self.Scale = float(S.number)
            except Exception as e:
                print(e)
        else:
            self.Scale = 0.0
    def setRring(self, S):
        if str(_RRad):
            try:
                self.ring_Radius = float(_RRad)
            except EXCEPTION as e:
                print(e)
        else:
            self.ring_Radius = 0.0

    
        
ob = simRing()
    
    

   










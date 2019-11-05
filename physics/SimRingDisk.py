from vpython import *


class simRing:
    def __init__(self):
        self.scene = canvas(width=1200, height=600)
        canvas.selected = self.scene
        self.Q_ring = 0.0
        self.tpi = 2 * pi
        self.ptsList = []
        self.Elist = []
        self.ptChargePOS = vector(0,0,0)
        self.ElectricField = vector(0,0,0)
        self.Scale = 0.02
        self.numberOFchargesInRing = 2
        self.K = 9e9
        self.Tstate = False
        self.scRun = False
        self.d_theta = self.tpi/100
        self.initInputs()
        self.Earrow=arrow(pos=vector(0,0,0),axis=vector(1,0,0),color=color.purple)
    
    def simulate(self):
        if len(self.scene.objects):
            for ob in self.scene.objects:
                ob.visible = False
        self.ringobj = ring(pos=vector(0,0,0),axis=vector(1,0,0), radius=self.ring_Radius,thickness=self.ring_Radius/10, color=color.red)
        self.theta = 0
        self.d_theta = self.tpi/self.numberOFchargesInRing
        self.deltaQ = self.Q_ring / self.numberOFchargesInRing
        self.ptsList = []
        self.Elist = []
        self.ElectricField = vector(0,0,0)
        while self.theta < self.tpi:
            self.ptsList = self.ptsList + [sphere(pos=self.ring_Radius*vector(0,cos(self.theta),sin(self.theta)),radius=self.ring_Radius/8, color=color.green)]
            self.theta = self.theta + self.d_theta
        self.ptcharge = sphere(pos=self.ptChargePOS, radius=self.ring_Radius/10, color=color.blue)
        for pts in self.ptsList:
            d = self.ptcharge.pos - pts.pos
            EforEach = self.K*self.deltaQ*norm(d)/mag(d)**2
            self.Elist = self.Elist + [{1:pts.pos,2:(self.Scale/mag(EforEach))*EforEach}]
            self.ElectricField = self.ElectricField + EforEach
        i = 0
        pArrows = []
        for E in self.Elist:
            pArrows += [self.createArrow(E)]
            if i==0:
                time.sleep(2)
            i += 1
        time.sleep(3)
        for a in pArrows:
            a.clear_trail()
        if self.ptcharge.pos == vector(0,0,0):
            self.ElectricField = vector(0,0,0)
        self.Earrow=arrow(pos=self.ptcharge.pos,axis=(self.Scale/mag(self.ElectricField))*self.ElectricField,color=color.purple, shaftwidth=float(self.ring_Radius/10))
        self.scRun = True

    def initInputs(self):
        wtext(pos=self.scene.caption_anchor,text="Enter Charge Q for Ring")
        self.scene.append_to_caption(' ') 
        self.Q_ring_Entry = winput(pos=self.scene.caption_anchor,bind=self.setQring)
        self.scene.append_to_caption(' ') 
        wtext(pos=self.scene.caption_anchor,text="Enter Radius for ring")
        self.scene.append_to_caption(' ') 
        self.Radius_Entry = winput(pos=self.scene.caption_anchor,bind=self.setRring)
        wtext(pos=self.scene.caption_anchor,text="Enter N for Delta Q (Q / N)")
        self.scene.append_to_caption(' ') 
        self.N_Entry = winput(pos=self.scene.caption_anchor,bind=self.setNchar)
        self.scene.append_to_caption('\n') 
        wtext(pos=self.scene.caption_anchor,text="Enter Position for Point Charge")
        self.scene.append_to_caption(' ') 
        self.ptChargePOS_Entry = winput(pos=self.scene.caption_anchor,type="string", bind=self.setPtchar)
        self.scene.append_to_caption(' ') 
        self.Escale_Label = wtext(pos=self.scene.caption_anchor,text="Enter E Scale for Q")
        self.scene.append_to_caption(' ') 
        self.Escale_Entry = winput(pos=self.scene.caption_anchor,bind=self.setEscale)

                
    def createArrow(self,d):
        return arrow(pos=d[1], axis=d[2], color=color.cyan, shaftwidth=float(self.ring_Radius/10))
    def setQring(self, S):
        if S.number:
            self.Q_ring = S.number
            print(self.Q_ring)
    def setPtchar(self, S):
        if S.text:
            try:
                ptsQ = str(S.text)
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
        if S.number:
            try:
                self.ring_Radius = float(S.number)
            except Exception as e:
                self.ring_Radius = float(0)
                print(e)
        else:
            self.ring_Radius = 0.0

    
        
ob = simRing()
    
    

   










from vpython import *
from tkinter import messagebox
from tkinter import *
import threading
import time
import sys

tpi = 2*pi

class simElecRing(threading.Thread):
  def __init__(self, _master):   
    self.master = _master
    self.Q_ring_Label = Label(self.master, text="Enter Q for ring")
    self.Escale_Label = Label(self.master, text="Enter Electric field scaling")
    self.Escale_Entry = Entry(self.master)
    self.N_Label = Label(self.master, text="Enter Number Of Charges In Ring")
    self.ptChargePOS_label = Label(self.master, text="Enter Position for point charge")
    self.N_Entry = Entry(self.master)
    self.ptChargePOS_Entry = Entry(self.master)
    self.Radius_Label = Label(self.master, text="Enter Radius for ring")
    self.Q_ring_Entry = Entry(self.master)
    self.Radius_Entry = Entry(self.master)
    self.Q_ring_Label.grid(row=0,sticky=E)
    self.Radius_Label.grid(row=1,sticky=E)
    self.Q_ring_Entry.grid(row=0, column=1)
    self.Radius_Entry.grid(row=1, column=1)
    self.N_Label.grid(row=2, sticky=E)
    self.ptChargePOS_label.grid(row=3, sticky=E)
    self.N_Entry.grid(row=2,column=1)
    self.ptChargePOS_Entry.grid(row=3,column=1)
    self.Escale_Label.grid(row=4)
    self.Escale_Entry.grid(row=4,column=1)
    self.SimButton = Button(self.master, text="Enter",  command=lambda: self.valueGet(self.Q_ring_Entry.get(), self.Radius_Entry.get(), self.N_Entry.get(), self.ptChargePOS_Entry.get(), self.Escale_Entry.get()))
    self.SimButton.grid(columnspan=5)
    self.frame = Frame(self.master,height=400, width=400)
    self.frame.grid_propagate(0)
    self.frame.grid(columnspan=6,sticky=N+E+W+S)
    self.msgOut = Label(self.frame, text="test\n test")
    self.msgOut.pack(fill=BOTH)
    self.msg = ""
    self.numberOFchargesInRing = 2
    self.K = 9e9
    self.d_theta = tpi/100
    self.Q_ring = 0.0
    self.ring_Radius = 0.0
    self.ptsList = []
    self.Elist = []
    self.ptChargePOS = vector(0,0,0)
    self.ElectricField = vector(0,0,0)
    self.Scale = 0.02
    self.Tstate = False
    self.scRun = False
  
  
  
  
  def valueGet(self, _Q_ring, _RRad, _Nu, _ptsQ, _Es):
    self.msg = ""
    if "e" in str(_Q_ring):
      _Q_ring = str(_Q_ring).split("e")
      self.Q_ring = float(_Q_ring[0]) * pow(10,int(_Q_ring[1]))
      self.msg += "\n\n" + "The Net Charge of Ring is " + str(self.Q_ring)
    elif "x" in str(_Q_ring):
      _Q_ring = str(_Q_ring).split("x")
      self.Q_ring = float(_Q_ring[0]) * pow(10,int(str(_Q_ring[1]).split("^")[1]))
      self.msg += "\n\n" + "The Net Charge of Ring is " + str(self.Q_ring)
    elif str(_Q_ring):
      try:
        self.Q_ring = int(_Q_ring)
        self.msg += "\n\n" + "The Net Charge of Ring is " + str(self.Q_ring)
      except EXCEPTION as e:
        self.msg += "\n\n" + "Charge of Ring Exeption " + str(e)
    else:
      self.Q_ring = 0.0
    if str(_RRad):
      try:
        self.ring_Radius = float(_RRad)
        self.msg += "\n\n" + "The Radius is " + str(self.ring_Radius)
      except EXCEPTION as e:
        self.msg += "\n\n" + "Radius Exeption " + str(e)
    else:
      self.ring_Radius = 0.0
    if str(_Nu):
      try:
        self.numberOFchargesInRing = int(_Nu)
        self.msg += "\n\n" + "Number of charges in Ring " + str(self.numberOFchargesInRing)
      except EXCEPTION as e:
        self.msg += "\n\n" + "N Charges in Ring Exeption " + str(e)
    else:
      self.numberOFchargesInRing = 2
    if str(_ptsQ):
      try:
        ptsQ = str(_ptsQ)
        self.ptChargePOS = vector(float(ptsQ.split(",")[0]), float(ptsQ.split(",")[1]), float(ptsQ.split(",")[2]))
        self.msg += "\n\n" + "The Point Charge Position is " + str(self.ptChargePOS)
      except EXCEPTION as e:
        self.msg += "\n\n" + "Point Charge Position Exeption Thrown " + str(e)
    else:
      self.ptChargePOS = vector(0,0,0)
    if str(_Es):
      try:
        self.Scale = float(_Es)
      except Exception as i:
        self.msg += "\n\n" + "Escale Exeption Thrown " + str(e)
      
    else:
      self.Scale = 0.1
    try:
      self.run(self.Tstate)
    except Exception as e:
      self.msg += "\n\n" + "Threading Exeption Thrown " + str(e)
  
  def simulate(self):
    if len(scene.objects):
      for ob in scene.objects:
        ob.visible = False
    self.ringobj = ring(pos=vector(0,0,0),axis=vector(1,0,0), radius=self.ring_Radius,thickness=self.ring_Radius/10, color=color.red)
    self.theta = 0
    self.d_theta = tpi/self.numberOFchargesInRing
    self.deltaQ = self.Q_ring / self.numberOFchargesInRing
    self.ptsList = []
    self.Elist = []
    self.ElectricField = vector(0,0,0)
    while self.theta < tpi:
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
    Earrow=arrow(pos=self.ptcharge.pos,axis=(self.Scale/mag(self.ElectricField))*self.ElectricField,color=color.purple, shaftwidth=float(self.ring_Radius/10))
    self.msg += "\n" + "The Electric Field at Point Charge is " + str(mag(self.ElectricField))
    self.update_msg()
    self.scRun = True

  def createArrow(self,d):
    return arrow(pos=d[1], axis=d[2], color=color.cyan, shaftwidth=float(self.ring_Radius/10))
  def run(self, state):
    if not state:
      self.Tstate = True
      self.simThread = threading.Thread(target=self.simulate())
      self.simThread.start()
      self.simThread.join()
    elif state:
      if self.simThread.is_alive():
        self.simThread._stop()
      self.simThread = threading.Thread(target=self.simulate())
      self.simThread.start()
      self.simThread.join()
  
  def update_msg(self):
    self.msgOut['text'] = self.msg

  def killcanvas(self):
    if messagebox.askokcancel("Quit", "You want to quit now?"):
      try:
        if self.simThread.is_alive():
          self.simThread._stop()
      finally:
        self.master.destroy()
        exit(0)

      


root = Tk()
obj = simElecRing(root)
root.protocol("WM_DELETE_WINDOW", obj.killcanvas)
root.mainloop()






